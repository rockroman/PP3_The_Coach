import re


class Player:
    """
    Class that creates players based
    on user Input and given parameters
    """
    def __init__(self):
        while True:
            self.name = input("Please input player name: ")
            if not re.match(r'^[a-zA-Z\s]{1,15}$', self.name):
                print(
                    'Name can be 15 characters long and contain'
                    ' only letters')
                continue
            break
        while True:
            try:
                self.age = input(
                        "please input player age"
                        "(values should be between 18-38):")
                self.age = int(self.age)
            except ValueError:
                print('Please use numeric digits.')
                continue
            if self.age < 18 or self.age > 38:
                print('Please enter value in range from 18 to 38')
                continue
            break
        while True:
            try:
                self.height = input(
                    "please input player height"
                    "(values should be between 160-230cm): ")
                self.height = int(self.height)
            except ValueError:
                print('Please use numeric digits.')
                continue
            if self.height < 160 or self.height > 230:
                print('Please enter value in range from 160 to 230cm')
                continue
            break
        while True:
            try:
                self.weight = input(
                        "please input player weight"
                        "(values should be between 60-130kg): ")
                self.weight = int(self.weight)
            except ValueError:
                print('Please use numeric digits.')
                continue
            if self.weight < 60 or self.weight > 130:
                print('Please enter value in range from 60 to 130kg')
                continue
            break

    def player_bmr(self):
        """
        Calculates player basic
        metabolic rate based on previous
        inputed parameters
        """
        bmr = 66.5 + (13.75 * self.weight) + (5.003 * self.height) -\
            (6.75 * self.age)
        return (round(bmr))

