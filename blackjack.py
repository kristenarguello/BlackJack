import random
global dealer, player, deck, values, suits, ranks
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

class Card:
    def __init__(self,num,simb):
        self.num = num
        self.simb = simb
        self.value = values[num]
    def __str__(self):
        return self.num + " of " + self.simb

class Deck:
    def __init__(self):
        self.baralho = []
        for s in suits:
            for r in ranks:
                self.baralho.append(Card(r,s))
    def shuffle(self):
        random.shuffle(self.baralho)
    def deal(self):
        return self.baralho.pop()

class Player:
    def __init__(self):
        self.mao = []
        self.soma = 0
    def compra(self,nova):
        self.mao.append(nova)
        if type(nova) == Card:
            if nova.num == 'Ace':
                n = 0
                while not n in [1,11]:
                    n = valor_ace()
                    if not n in [1,11]:
                        print('Please insert 1 or 11')
                self.soma += n
            else:
                self.soma += nova.value
        return self.soma
    def cards(self):
        print('-CARDS-')
        for c in self.mao:
            print(c)

class Dealer:
    def __init__(self):
        self.mao = []
        self.soma = 0
    def compra(self,nova):
        self.mao.append(nova)
        if type(nova) == Card:
            if nova.num == 'Ace':
                if self.soma + 11 > 21:
                    self.soma += 1
                else:
                    self.soma += 11
            else:
                self.soma += nova.value
        return self.soma
    def show_one(self):
        print(f'\033[4;31m{self.mao[0].value}\033[m')
        print(self.mao[0])
        print('-HIDDEN CARD-')
        print('xx')
        print('xxxxxx xx xxxxxx')
    def cards(self):
        print('-CARDS-')
        for c in self.mao:
            print(c)
    def buy_onemore(self):
        if self.soma<16 and self.soma<21:
            return True
        else:
            return False

def valor_ace():
    while True:
        try:
            ace = int(input('Please insert the value of Ace (1 or 11)'))
        except:
            print('Please insert a numeric valid number')
            continue
        else:
            return ace

def blackjack(p,d):
    if p == 21 and not d==21:
        print('\033[4;33\nPlayer got BLACKJACK! You won!\n\033[m')
        return True
    elif (not p == 21) and d==21:
        print('\033[4;33\nSorry, dealer got BLACKJACK\n\033[m')
        dealer.cards()
        return True
    elif p == 21 and d == 21:
        print('\033[4;33\nBoth of you got BLACKJACK. But Dealer gets the prize\n\033[m')
    else: return False

def lost(p,d):
    if p>21 and not d>21:
        print('\033[4;33m\nPlayer, you lost, you folded!\033[m')      
        return True
    elif not p>21 and d>21:
        print('\033[4;33m\nPlayer, you won! Dealer folded!\033[m')      
        return True
    elif p>21 and d>21:
        print('\033[4;33m\nBoth of you folded! Dealer won\033[m')      
        return True
    else: return False

def restart(p,d):
    if blackjack(p,d) or lost(p,d):
        inp = 'null'
        while True:
            inp = str(input('Do you wanna keep playing? (Y or N)'))
            inp = inp.upper()
            if inp == 'Y':
                print("\n"*1000)
                return 1
            elif inp == 'N': 
                return -1
    else: return 0

def restart_two(p,d):
    if lost(p,d):
        inp = 'null'
        while True:
            inp = str(input('Do you wanna keep playing? (Y or N)'))
            inp = inp.upper()
            if inp == 'Y':
                print("\n"*1000)
                return 1
            elif inp == 'N': 
                return -1
    else: return 0

def who_won(p,d):
    if p>d:
        print('\033[4;30m\nEND OF GAME!\033[m')        
        print(f'PLAYER VALUE: \033[4;31m{p}\033[m')
        player.cards()
        print('-----------------')
        print(f'DEALER VALUE: \033[4;34m{p}\033[m')        
        dealer.cards()
        print('\033[4;33m\nCongratulations! Player won!\033[m')        
    elif d>p:
        print('\033[4;30m\nEND OF GAME!\033[m')        
        print(f'PLAYER VALUE: \033[4;31m{p}\033[m')        
        player.cards()
        print('-----------------')
        print(f'DEALER VALUE: \033[4;34m{p}\033[m')        
        dealer.cards()
        print('\033[4;33m\nSorry, dealer won...\033[m')  
    else:
        print('\033[4;30m\nEND OF GAME!\033[m')
        print(f'PLAYER VALUE: \033[4;31m{p}\033[m')        
        player.cards()
        print('-----------------')
        print(f'DEALER VALUE: \033[4;34m{p}\033[m')        
        dealer.cards()
        print('\033[4;33m\nIt was a tie! So dealer won this round\033[m')      
    inp = 'null'
    while True:
        inp = str(input('\nDo you wanna keep playing? (Y or N)'))
        inp = inp.upper()
        if inp == 'Y':
            print("\n"*1000)
            return True
        elif inp == 'N': 
            print('\nThanks for playing!')
            return False

def hit_stand():
    ans = 'null'
    while not ans == 'HIT' and not ans == 'STAND':
        ans = str(input('\nHIT or STAND?'))
        ans = ans.upper()
    if ans == 'HIT':
        return True
    else:
        return False

while True:
    deck = Deck()
    deck.shuffle()
    dealer = Dealer()
    player = Player()

    print(f"\nLet's play \033[4;30mBLACKJACK\033[m")

    print(f'\033[4;34mPLAYER\033[m')
    player.compra(deck.deal())
    player.compra(deck.deal())
    print(f'\033[4;34m{player.soma}\033[m')
    player.cards()
    print('-----------------')
    print(f'\033[4;31mDEALER\033[m')    
    dealer.compra(deck.deal())
    dealer.compra(deck.deal())
    dealer.show_one()

    play = restart(player.soma,dealer.soma)
    if play == 1:
        continue
    elif play==-1:
        print('Thanks for playing!')
        break
    elif play==0:
        pass

    compraP = hit_stand()
    if not compraP:
        print(f"\n\n\033[4;30mSTAND\033[m")
        d_pode_comprar = dealer.buy_onemore()
        while d_pode_comprar:
            print(f"\033[4;31m\nDEALER'S TURN\033[m")
            print(f"\033[4;31m{dealer.compra(deck.deal())}\033[m")
            dealer.cards()
            d_pode_comprar = dealer.buy_onemore()
        play = restart_two(player.soma,dealer.soma)
        if play == 1:
            continue
        elif play==-1:
            print('\nThanks for playing!')
            break
        elif play==0:
            value = who_won(player.soma,dealer.soma)
            if value:
                continue
            else:
                break
    while compraP:
        print(f"\n\n\033[4;30mHIT ME!\033[m")
        print(f'\033[4;34m{player.compra(deck.deal())}\033[m')
        player.cards()
        print('\n')
        play = restart_two(player.soma,dealer.soma)
        if play == 1:
            break
        elif play==-1:
            print('\nThanks for playing!')
            break
        elif play==0:
            compraP = hit_stand()
            pass
        elif player.soma == 21:
            compraP = False
            pass
        if not compraP:
            print(f"\n\n\033[4;30mSTAND\033[m")
            d_pode_comprar = dealer.buy_onemore()
            while d_pode_comprar:
                print(f"\033[4;31m\nDEALER'S TURN\033[m")
                print(f'\033[4;31m{dealer.compra(deck.deal())}\033[m')
                dealer.cards()
                d_pode_comprar = dealer.buy_onemore()
    if play == 1:
        continue
    if play == -1:
        break
    play = restart_two(player.soma,dealer.soma)
    if play == 1:
        continue
    elif play==-1:
        print('\nThanks for playing!')
        break
    elif play==0:
        value = who_won(player.soma,dealer.soma)
        if value:
            continue
        else:
            break
