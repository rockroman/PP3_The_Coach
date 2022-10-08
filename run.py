from player import Player
import os


def start_coach():
    global MY_PLAYERS
    print("inputs for player1..\n")
    player1 = Player()
    print("inputs for player2..\n")
    player2 = Player()
    MY_PLAYERS = [player1, player2]
    os.system('cls')