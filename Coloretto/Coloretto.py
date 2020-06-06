import random

class BoardState:
    
    def __init__(self, num_players):
        self.deck = sorted((list(range(1, 9)) * 8) +[8,8,9,9,9])
        self.aux_deck = list((range(1,8)))
        self.field = [[] for x in range(num_players)]
        self.lastRound = False
        for x in range(num_players):
            tmpstr = str(self.aux_deck).strip('[]')
            card = int(input("Player " + str(x) + " please choose one of the following cards: " + tmpstr + "\n"))
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
        self.turn = 0
        self.playRound()
        
    def newRound(self):
        return
    
    def printStatus(self):
        print("Starting new round", players.out)
        return
    
    def playRound(self):
        
        while board.lastRound == False:

            self.newRound()
            
            while not all(players.out):
                
                self.turn = (self.turn + 1) % num_players
                
                action = input("Would you like to take a pile or draw a card? \n").lower()
                if action == "draw":
                    
                    topcard = board.deck.pop()

                    self.placeCard(topcard)

                    print(board.field)

                elif action == "take":
                    pass                
        
        return


    def placeCard(self, topcard):
        valid = []
        for i in range(len(board.field)):
            if len(board.field[i]) < 3:
                valid.append(i)
        while True:
            placement = int(input("Enter an pile to place "+ str(topcard) +": \nValid locations are "+ str(valid)+"\n"))
            if placement in valid:
                board.field[placement].append(topcard)
                break
            else:
                print("That pile is not available, please choose again.")

    def takeCard(self):
        pass


num_players = 4

players = PlayerState(num_players)
board = BoardState(num_players)
game = GameState(num_players)




game = GameState(num_players)