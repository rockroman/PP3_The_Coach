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
    pick_training()
    # print(player_1.active_m_r)


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
        'Gym', 'Cardio', 'Shooting', 'Ball_handling', 'Dueling',
        'Driblling', 'Defense_Rebounding', 'Pick_n_roll', 'Pivoting']
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


start_coach()


