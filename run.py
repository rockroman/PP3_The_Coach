from random import randint
from player import Player
import requests

import click


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
    get_player_meal()
    player_nutrition_value()
    player_nutrition_score()

    print(player_1.train_value)
    print(player_1.active_m_r)
    print(player_1.nutrition_score)
    print(player_2.train_value)
    print(player_2.active_m_r)
    print(player_2.nutrition_score)
    

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
                 (player.train_value * 0.37)
            player.train_value = round(player.train_value)
    return player.train_value


def pick_food_options():
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
    chosed_meals = []
    while num > 0:
        while True:
            try:
                chosed = input('choose meal number: ')
                chosed = int(chosed)
            except ValueError:
                print("Please choose numeric digits")
                continue
            if chosed < 0 or chosed > len(menu)-1:
                print("please choose only number assigned to meal")        
                continue
            break
        chosed_meals.append(menu[chosed])
        num -= 1

    return chosed_meals


def get_player_meal():
    """
    function assigns each player with 
    food option choosed by User
    """
    for play in my_players:
        print("please choose " + play.name.upper() + " meals for today")
        play.meals = pick_food_options()
        print("you choosed:-->", play.meals)
        player_meals = play.meals
        print("Calculating player nutrition value...\n")

    return player_meals


def get_meal_value(meal):
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


def player_nutrition_value():
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


def player_nutrition_score():
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

    return i.nutrition_score


start_coach()
