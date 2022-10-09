import click
from player import Player


my_players = []


def start_coach():
    """
    Main function that runs
    the game
    """
    print("inputs for player1..\n")
    player_1 = Player()
    my_players.append(player_1)
    print("inputs for player2..\n")
    player_2 = Player()
    my_players.append(player_2)
    clrscr()
    player_active_metabolic_rate()
    get_player_trained()
    print(player_1.training)


def clrscr():
    """
    Clear screen using click.clear() function
    """
    click.clear()


def player_active_metabolic_rate():
    """
    Calculating active_metabolic_rate
    for each player from players array
    """
    for i in my_players:
        i.active_m_r = round(Player.player_bmr(i) * 1.3)
        amr = i.active_m_r

    return amr


def pick_training():
    """
    User can pick training from
    enumerated list
    """
    print("here are the training options...\n")
    trainings = [
        'GYM', 'CARDIO', 'SHOOTING', 'BALL_HANDLING', 'DUELING',
        'DRIBLLING', 'DEFENSE_REBOUNDING', 'PICK_N_ROLL', 'PIVOTING']
    for i, j in enumerate(trainings):
        print(i, j)
    num = 3
    chosed_training = []
    while num > 0:
        while True:
            try:
                chosed = input('choose training number: ')
                chosed = int(chosed)
            except ValueError:
                print("Please choose numeric digits")
                continue
            if chosed < 0 or chosed > len(trainings)-1:
                print("please choose only number assigned to trainings")
                continue
            break
        chosed_training.append(trainings[chosed])
        num -= 1

    return chosed_training


def get_player_trained():
    """
    Assigns training option
    to each player and gives
    instance attribute to subclas  
    """
    for player in my_players:
        print("pick a training option for", player.name.upper())
        player.training = pick_training()
        print("you choosed: ", player.training)


# Variables that will give choosed training strings value
#  basic training
CARDIO = 30
GYM = 25
SHOOTING = 30
# intermediate training
BALL_HANDLING = 25
DRIBLLING = 30
DUELING = 45
# advanced training
PICK_N_ROLL = 45
DEFENSE_REBOUNDING = 40
PIVOTING = 30



start_coach()


