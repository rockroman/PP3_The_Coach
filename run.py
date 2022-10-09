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
    player_train_value()
    print(player_1.train_value)


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
    print("Note!Higher the training number")
    print("more Value it brings")
    print("Don't overtrain the player")
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


# holds trainings assigned to each player
my_players_training = []


def get_player_trained():
    """
    Assigns training option
    to each player and gives
    instance attribute to subclass
    """
    for player in my_players:
        print("pick a training option for", player.name.upper())
        player.training = pick_training()
        my_players_training.append(player.training)
        print("you choosed:--> ", player.training, "\n")
        

# Variables that will give choosed training strings value
#  basic training
CARDIO = 25
GYM = 25
SHOOTING = 25
# intermediate training
BALL_HANDLING = 30
DRIBLLING = 30
DUELING = 45
# advanced training
PICK_N_ROLL = 45
DEFENSE_REBOUNDING = 40
PIVOTING = 30


def player_train_value():
    """
    calculating player train value
    based on training choices and
    reduces value if player gets overtrained
    """
    for player in my_players:
        player.train_value = []
        for j in player.training:
            player.train_value.append(globals()[j])
        player.train_value = sum(player.train_value)
        if player.train_value > 100:
            player.train_value = player.train_value -\
                 (player.train_value * 0.38)
            player.train_value = round(player.train_value)
    return player.train_value


start_coach()
