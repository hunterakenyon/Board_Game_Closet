class BoardState:
    
    def __init__(self, num_players):
        self.deck = sorted((list(range(1, 9)) * 8) +[8,8,9,9,9])
        self.aux_deck = (range(1,8))
        self.field = [[] for x in range(num_players)]
        self.lastRound = False
        
    
    def newRound(self):
        return
        
        
class PlayerState:
    
    def __init__(self, num_players):
        self.claims = {x:{y:0 for y in range(9)} for x in range(num_players)}
        self.out = [False for x in range(num_players)]
        self.score = [0 for x in range (num_players)]
        
        
    