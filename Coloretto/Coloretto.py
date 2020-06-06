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
        self.num_players = num_players
        self.deck = board.deck
        
    def newRound(self):
        return
    
    def printStatus(self):
        return
    
    def playRound(self):
        
        while board.lastRound == False:
            
            self.newRound()
            
            while any(players.out):
                
                self.turn = (self.turn + 1) % self.num_players
                
                action = input("Would you like to take a pile or draw a card? \n").lower()
                if action == "draw":
                    
                    topcard = self.deck.pop()
                    placement = int(input("Which pile would you like to place the card in?\n"))
                    
                    return
                elif action == "take":
                    return
                
                topcard = self.deck.pop()
                
                pass
            
            
        
        return
    
    

num_players = 4

players = PlayerState(num_players)
board = BoardState(num_players)
game = GameState(num_players)




game = GameState(num_players)