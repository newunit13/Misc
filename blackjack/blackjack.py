from deck import Deck
from player import Player

DECK    = Deck()
RUNNING = True

print("""

###--------------------------------------------###
##                                              ##
##                                              ##
##      Welcome to the game of Black Jack!      ##
##                                              ##
##                                              ##
###--------------------------------------------###
    
""")

def play_again():
    r = input("Would you like to play again? (Y or N)")

    if r.lower() in ['n', 'no']:
        return False
    return True


while True:
    player_count = 0
    while player_count not in [x for x in range(1,9)]:
        try:
            player_count = int(input("How many are playing? (Max 8): "))
        except ValueError:
            print("\n\n**Please enter a valid number**\n")
        
    players = []
    for _ in range(player_count):
        players.append(Player())
    
    dealer = Player()
    
        


    if not play_again():
        break

