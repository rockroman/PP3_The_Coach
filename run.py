"""
random variable generator
"""
from random import randint
import click
import validate as val
from player import Player
import requests
import time
import sys
from data import insert_rows, WK1, show_table1, show_table2,\
        user_score, insert_rows2, WK3
from colors import Fore
from typing import List


my_players = []


def start_coach() -> None:
    """
    Main function that runs
    the game
    """
    val.program_title()
    create_players()
    player_active_metabolic_rate()
    insert_rows(my_players)
    clrscr()
    val.slow_print("Here is your Team")
    show_table1()
    get_player_trained()
    clrscr()
    player_train_value()
    get_player_meal()
    clrscr()
    print(Fore.GREEN + "Your result will be ready in 15 seconds")
    player_nutrition_value()
    clrscr()
    val.slow_print("Please wait until Score is calculated ")
    player_nutrition_score()
    insert_rows2(my_players)
    show_table2()
    for i in my_players:
        overall_player_score(i)
    team_preformance_score()
    end_or_play_again()


def welcome() -> None:
    """
    welcome message and a program description
    by using ASCII art
    """
    clrscr()
    line1 = "   Welcome to     "
    val.slow_print(line1)
    time.sleep(1.2)
    val.program_title()
    line2 = """
Program that will determine performance
percentage of the Team that you created
'The Coach' will give you a chance to create
a Team of 5 Basketball players.
You will:
Assign each player with 3 training options
(Each training option has VALUE)
Assign food intake with 3 options for a player
(Each Meal option has VALUE)
The result will be a percentage how well
would your team perform based on your instructions
ARE YOU READY?
        """
    val.slow_print(line2)
    time.sleep(1)
    while True:
        try:
            answer = input(
                f"{Fore.GREEN}"+"1)Proceed\n"f"{Fore.RED}"+"2)Exit program \n"
                f"{Fore.WHITE}")
            answer = int(answer)
        except ValueError:
            print(Fore.RED + "Please choose between 1 or 2")
            continue
        if answer > 2 or answer < 1:
            print(Fore.RED + "Please choose between 1 or 2")
            continue
        break
    if answer == 1:
        val.display_menu()
    elif answer == 2:
        sys.exit()


def end_or_play_again() -> None:
    """
    user can choose to run the program again
    or exit
    """
    val.slow_print("THANK YOU FOR BEEING 'THE COACH")
    val.slow_print("would you like to: ")
    status = input(
            f'{Fore.GREEN}' + "1)Go again\n" + f"{Fore.RED}" + "2)Exit \n"
            f"{Fore.WHITE}")
    while status not in ("1", "2"):
        print("Please choose between 1 or 2")
        status = input(
            f'{Fore.GREEN}' + "1)Go again\n" + f"{Fore.RED}" + "2)Exit \n"
            f"{Fore.WHITE}")
    if status == "1":
        start_coach()
    elif status == "2":
        sys.exit()


def clrscr() -> None:
    """
    Clear screen using click.clear() function
    """
    click.clear()


def create_players() -> None:
    """
    creates team of players from
    a Player class and appends each player to
    a list of players
    """
    my_players.clear()
    WK1.batch_clear(['A2:E6'])
    WK3.batch_clear(['A2:D6'])
    for i in range(1, 6):
        player = f"player{i}"
        val.slow_print(f"Please enter values for player{i}")
        player = Player()
        my_players.append(player)
        clrscr()
        val.program_title()


def player_active_metabolic_rate() -> int:
    """
    Calculating active_metabolic_rate
    for each player from players array
    """
    for i in my_players:
        i.active_m_r = round(Player.player_bmr(i) * 1.3)
        amr = i.active_m_r

    return amr


def pick_training() -> List[str]:
    """
    User can pick training from
    enumerated list
    """
    trainings = [
        'GYM', 'CARDIO', 'SHOOTING', 'BALL_HANDLING', 'DUELING',
        'DRIBLLING', 'DEFENSE_REBOUNDING', 'PICK_N_ROLL', 'PIVOTING']
    for i, j in enumerate(trainings):
        print(i, j)
        print()
    num = 3
    option = 1
    chosed_training = []
    while num > 0:
        while True:
            try:
                chosed = input(
                 f"{Fore.GREEN}" + f"OPTION {option}/3 ""\n"
                 f"{Fore.WHITE}" + "choose number with  training option: \n ")
                chosed = int(chosed)
            except ValueError:
                print(Fore.RED + "Please choose numeric digits")
                continue
            if chosed < 0 or chosed > len(trainings)-1:
                print(Fore.RED + "please choose only number\
 assigned to trainings")
                continue
            break
        chosed_training.append(trainings[chosed])
        num -= 1
        option += 1

    return chosed_training


# holds trainings assigned to each player
my_players_training = []


def get_player_trained() -> None:
    """
    Assigns training option
    to each player and gives
    instance attribute to subclass
    """
    note = """
YOU CAN NOW ASSIGN A TRAINING TO EACH PLAYER
NOTE! HIGHER THE TRAINING NUMBER
MORE VALUE IT BRINGS.
Don't overtrain the player
    """
    num = 1
    val.slow_print(note)
    for player in my_players:
        print("here are the training options...\n")
        line = (f"Pick 3 training options for,{player.name.upper()}")
        val.slow_print(line)
        print('#######################################')
        player.training = pick_training()
        my_players_training.append(player.training)
        print("you choosed:--> ", player.training, "\n")
        time.sleep(1.2)
        clrscr()
        num += 1


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


def player_train_value() -> int:
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
                 (player.train_value * 0.37)
            player.train_value = round(player.train_value)
    return player.train_value


def pick_food_options() -> List[str]:
    """
    displays range of meals for user
    to choose for player by enumerating them in order
    """
    menu = ['Yoghurt 200g ,2 bananas and 80g uf nuts',
            'Granola 150g  and  Greek yogurt 250g',
            'butter 50g whole grain bagel,2 boiled eggs,cottage cheese',
            'Grain toast 150g ,160g shaved ham , tomato and mushrooms\
 2 avocado',
            'ratatouille 280g cod fillet and 200g feta tomato salad',
            'seasonal vegetables 160g pasta 90g white sauce \
 and 220g of salmon',
            'avocado salad 230g beef steak and 250g of baked potatoes',
            'Broccoli ,250g grilled chicken breasts,180g rice and Quinoa \
 and Mozzarella Salad',
            'grilled pepper 200g of chicken breasts and 70g of crusty bread',
            'Tuna ,120g pasta ,green beans,80g feta cheese',
            'Burrito  with lean mince beans 50g corn \
 and tomato and onion salad',
            'Egg frittata with sliced sweet potato  zucchini \
 capsicum and feta cheese']
    for i, j in enumerate(menu):
        print(i, j)
    num = 3
    print("\n")
    option = 1
    chosed_meals = []
    while num > 0:
        while True:
            try:
                chosed = input(
                 f"{Fore.GREEN}" + f"OPTION {option}/3""\n"
                 f"{Fore.WHITE}" + "Choose number assigned to a meal:\n")
                chosed = int(chosed)
            except ValueError:
                print(Fore.RED + "Please choose numeric digits")
                continue
            if chosed < 0 or chosed > len(menu)-1:
                print(Fore.RED + "please choose only number assigned to meal")
                continue
            break
        chosed_meals.append(menu[chosed])
        num -= 1
        option += 1

    return chosed_meals


def get_player_meal() -> List[str]:
    """
    function assigns each player with
    food option choosed by User
    """
    note = """
You can now assign 3 meals for
each player!NOTE EACH MEAL HAS CALORIC VALUE
SO TRY AND BALANCE THE MEALS.
    """
    val.slow_print(note)
    for play in my_players:
        val.slow_print(f"please choose 3 meals for {play.name.upper()} today:")
        print('#######################################')
        play.meals = pick_food_options()
        time.sleep(0.5)
        clrscr()
        print("you choosed: ")
        for i in play.meals:
            print("->>>", i)
        time.sleep(1.5)
        player_meals = play.meals
        clrscr()
        print("Calculating player nutrition value...\n")

    return player_meals


def get_meal_value(meal: str) -> int:
    """
    Funtion that gets caloric value of meal
    choosed by user by calling "Calorie Ninja API"
    """
    query = meal
    api_url = 'https://api.calorieninjas.com/v1/nutrition?query='
    my_key = {'X-Api-Key': 'FmFFagHTyI87GX8IerJW7w==0J4N2eWYlplpbfQX'}
    response = requests.get(api_url + query, headers=my_key, timeout=5)
    if response.status_code == requests.codes.ok:  # pylint: disable=no-member
        response = response.json()
    else:
        print("Error:", response.status_code, response.text)
    nut_current = []
    for item in response["items"]:
        nut_current.append(item["calories"])

    nut_current = sum(nut_current)
    return round(nut_current)


def player_nutrition_value() -> List[str]:
    """
    function that sums caloric value of all meals
    assigned to each player by using a callback function
    """
    for i in my_players:
        i.calorie_value = []
        for j in i.meals:
            value = get_meal_value(j)
            i.calorie_value.append(value)
        i.calorie_value = sum(i.calorie_value)
        player_calorie_value = i.calorie_value

    return player_calorie_value


def player_nutrition_score() -> int:
    """
    function that compares active metabolic rate of player
    with caloric value of food intake and assignes nutrition score to
    player adjusting it in case of too many calories taken and
    if insuficient calories are taken
    """
    for i in my_players:
        if i.calorie_value > (i.active_m_r + (i.active_m_r * 0.22)):
            i.nutrition_score = randint(61, 70)
        elif i.calorie_value < (i.active_m_r - (i.active_m_r * 0.27)):
            i.nutrition_score = randint(51, 60)
        elif i.calorie_value == i.active_m_r:
            i.nutrition_score = 100
        else:
            i.nutrition_score = randint(80, 92)
            nutrition_score = i.nutrition_score

    return nutrition_score


def overall_player_score(each) -> int:
    """
    function tahat calculates overall
    player score and will be used in loop
    for each player
    """
    each.overall_score = each.nutrition_score + each.train_value
    return each.overall_score


def team_preformance_score() -> int:
    """
    get final team score bay summ of all players
    score and give the result in precentages
    """
    team_score = []
    for i in my_players:
        team_score.append(i.overall_score)
    team_score = sum(team_score)/10
    val.slow_print("BASED ON YOUR INPUT AN DECISIONS..\n")
    print(Fore.GREEN + f"YOUR TEAM PERFOMANCE WOULD BE {team_score}%")
    user_score(team_score)


def main():
    """
    runs all the functions
    """
    welcome()
    start_coach()


if __name__ == "__main__":
    main()
