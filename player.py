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