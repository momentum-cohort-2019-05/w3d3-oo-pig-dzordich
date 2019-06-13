from random import randint

class Player:
    def __init__(self, name, score=0,):
        self.score = score
        self.name = name

    def is_winner(self):
        if self.score > 100:
            return True
        return False

    def add_to_score(self, round_score):
        self.score += round_score

    def __eq__(self, other):
        return self.name == other
    


        
class Dice:

    ##Approximately replicates a roll of an evenly weighted die. Plus output.
    def roll(self):
        r = randint(1, 6)
        if r == 1:
            print("Oh No! You rolled a 1! You don't score anything this round.")
            return 0
        print(f"You rolled a {r}!")
        return r   