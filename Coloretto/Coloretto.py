import random

class BoardState:
    
    def __init__(self, num_players):
        self.deck = sorted((list(range(1, 9)) * 8) +[8,8,9,9,9])
        self.aux_deck = list((range(1,8)))
        self.field = [[] for x in range(num_players)]
        self.lastRound = False
        for x in range(num_players):
            tmpstr = str(self.aux_deck).strip('[]')
            while True:
                try:
                    card = int(input("Player " + str(x) + " please choose one of the following cards: " + tmpstr + "\n"))
                    if card in self.aux_deck:
                        break
                except:
                    print("Please enter a valid option. ")
            self.aux_deck.remove(card)
            players.add_card(x, card)
        self.deck += self.aux_deck
        random.shuffle(self.deck)
        
        
class PlayerState:
    
    def __init__(self, num_players):
        self.claims = {x:{y:0 for y in range(1,10)} for x in range(num_players)}
        self.out = [False for x in range(num_players)]
        self.score = [0 for x in range (num_players)]
        
    def add_card(self, player, card):
        self.claims[player][card] += 1
        
        
class GameState:
    
    def __init__(self, num_players):
        self.currentPlayer = 0
        self.lastOut = 0
        self.playRound(num_players)
        
    def newRound(self, num_players):
        board.field = [[] for n in range(num_players)]
        players.out = [False for n in range(num_players)]
        self.currentPlayer = self.lastOut - 1
        
    
    def printStatus(self):
        print("Starting new round", players.out)
        return
    
    def playRound(self, num_players):
        
        while board.lastRound == False:

            self.newRound(num_players)
            
            while not all(players.out):
                self.currentPlayer = (self.currentPlayer + 1) % num_players
                if players.out[self.currentPlayer]:
                    continue
                fieldSize = [len(n) for n in board.field]
                #print(board.field[0], board.field.count(board.field[0]), len(board.field))
                if len(board.field[0]) == 3 and fieldSize.count(fieldSize[0]) == len(board.field):

                    for i in range(len(board.field)):
                        print(i, board.field[i])

                    self.takePile()

                else:                                       
                    while True:
                        action = input("Would you like to take a pile or draw a card? \n").lower()
                        if action == "draw":
                            if len(board.deck) == 15:
                                print("Last turn!")
                                board.lastRound = True
                            topcard = board.deck.pop()
                            self.placeCard(topcard)
                            print(board.field)
                            break

                        elif action == "take":

                            for i in range(len(board.field)):
                                print(i, board.field[i])

                            self.takePile()
                            break
                        else:
                            print("Please enter \"draw\" or \"take\".")

        return


    def placeCard(self, topcard):
        valid = []
        for i in range(len(board.field)):
            if len(board.field[i]) < 3:
                valid.append(i)
        while True:
            try:
                placement = int(input("Enter a pile to place "+ str(topcard) +": \nValid locations are "+ str(valid)+"\n"))
                if placement in valid:
                    board.field[placement].append(topcard)
                    break
            except:
                print("That pile is not available, please choose again.")

    def takePile(self):
        valid = [n for n in range(len(board.field))]
        while True:
            pile = int(input("Select which pile you would like to take: \nValid piles are " + str(valid) +"\n"))
            if pile in valid:
                players.out[self.currentPlayer] = True
                selection = board.field.pop(pile)
                for card in selection:
                   # players.claims[self.currentPlayer][card] += 1
                    players.add_card(self.currentPlayer,card)
                self.lastOut = self.currentPlayer
                break
            else:
                print("That is not a valid pile. Please choose again.")



num_players = 4

players = PlayerState(num_players)
board = BoardState(num_players)
game = GameState(num_players)




game = GameState(num_players)