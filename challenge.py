# Creating RPG character===================================
class Character:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def display_status(self):
        input(
            print(f'Name: {self.name}\nHealth: {self.health}\nAttack: {self.attack}'))
