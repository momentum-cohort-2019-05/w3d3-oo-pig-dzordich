from gameClasses import Player, Dice

##Initializes the game
name = input("Input player 1's name. ")
name2 = input("Input player 2's name. Press enter to play the computer. ")

player1 = Player(name)
if name2 == "":
    player2 = Player("CPU")
else:
    player2 = Player(name2)
dice = Dice()
gameOver = False
players = [player1, player2]


def round_of_game(player):
    keep_rolling = True
    round_score = 0
    while keep_rolling:
        print(f"Your score so far this round is {round_score}.")
        a = input("Hit ENTER to roll dice. Input H to hold. ")
        roll_score = 0
        if a == "":
            roll_score = dice.roll()
            
            if roll_score == 0:
                round_score = 0
                return round_score
            round_score += roll_score
        else:
            keep_rolling = False
    return round_score

##Slightly different code used for player2 if player2 is the computer. Doesn't need input.
def computer_round(player):
    keep_rolling = True
    round_score = 0
    while keep_rolling:
        roll_score = dice.roll()
        if roll_score == 0:
            round_score = 0
            return round_score
        if roll_score >= 5 or round_score > 12:
            keep_rolling = False
    print(f"CPU's score that round: {round_score}")
    return round_score

def game():
    player1.score = 0
    player2.score = 0
    gameOver = False
    while not gameOver:
        for p in players:
            print(f"{player1.name}: {player1.score} | {player2.name}: {player2.score}")
            score_to_add = 0
            print(f"{p.name}'s turn.")
            if p == "CPU":
                score_to_add = (computer_round(p))
                p.add_to_score(score_to_add)
                print(f"CPU's score that round: {p.score}")
            else:
                score_to_add = (round_of_game(p))
                p.add_to_score(score_to_add)
                print(f"{p.name}'s score that round: {p.score}")
            if p.score > 100:
                winner = p
                gameOver = True
                break
    print(f"{winner.name} won!!")
    hamburger = input("Would you like to play again? Input y for yes or n for no. ")
    if hamburger.lower() == "y":
        game()
    else:
        print("Thanks for playing")

        
game()
