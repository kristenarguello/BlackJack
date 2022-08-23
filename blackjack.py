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
        print('-SHOWN CARD-')
        print(self.mao[0].value)
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
        print('Player got BLACJACK! You won!')
        return True
    elif (not p == 21) and d==21:
        print('Sorry, dealer got BLACKJACK')
        dealer.cards()
        return True
    elif p == 21 and d == 21:
        print('Both of you got BLACKJACK. But Dealer gets the prize')
    else: return False

def lost(p,d):
    if p>21 and not d>21:
        print('Player, you lost, you folded')
        return True
    elif not p>21 and d>21:
        print('Player, you won! Dealer folded')
        return True
    elif p>21 and d>21:
        print('Both of you folded! So, Dealer won')
        return True
    else: return False

def restart(p,d):
    if blackjack(p,d) or lost(p,d):
        inp = 'null'
        while True:
            inp = str(input('Do you wanna keep playing? (Y or N)'))
            inp = inp.upper()
            if inp == 'Y':
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
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                return 1
            elif inp == 'N': 
                return -1
    else: return 0

def who_won(p,d):
    if p>d:
        print('PLAYER VALUE: ', p)
        player.cards()
        print('-----------------')
        print('DEALER VALUE: ', d)
        dealer.cards()
        print('\nCongratulations! Player won!')
    elif d>p:
        print('PLAYER VALUE: ', p)
        player.cards()
        print('-----------------')
        print('DEALER VALUE: ', d)
        dealer.cards()
        print('\nSorry, Dealer won...')
    else:
        print('PLAYER VALUE: ', p)
        player.cards()
        print('-----------------')
        print('DEALER VALUE: ', d)
        dealer.cards()
        print('\nIt was a tie. So, Dealer won this round')
    inp = 'null'
    while True:
        inp = str(input('Do you wanna keep playing? (Y or N)'))
        inp = inp.upper()
        if inp == 'Y':
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            return True
        elif inp == 'N': 
            print('Thanks for playing!')
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

    print("Let's play BLACKJACK!")
    print('\nPLAYER')
    player.compra(deck.deal())
    player.compra(deck.deal())
    print(player.soma)
    player.cards()
    print('-----------------')
    print('DEALER')
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
        print('\n\nSTAND!\n')
        d_pode_comprar = dealer.buy_onemore()
        while d_pode_comprar:
            print("DEALER'S TURN\n")
            print(dealer.compra(deck.deal()))
            dealer.cards()
            d_pode_comprar = dealer.buy_onemore()
        play = restart_two(player.soma,dealer.soma)
        if play == 1:
            continue
        elif play==-1:
            print('Thanks for playing!')
            break
        elif play==0:
            value = who_won(player.soma,dealer.soma)
            if value:
                continue
            else:
                break
    while compraP:
        print('\n\nHIT ME!')
        print(player.compra(deck.deal()))
        player.cards()
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
            print('\n\nSTAND!\n')
            d_pode_comprar = dealer.buy_onemore()#ate linha 254 pode tirar, depende do quintana
            while d_pode_comprar:
                print("DEALER'S TURN\n\n")
                print(dealer.compra(deck.deal()))
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
