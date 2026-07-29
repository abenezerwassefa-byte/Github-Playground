class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        return f'The {self.name} is eating people!!!'

    def sleep(self):
        return f'Hold on, I think the {self.name} is sleeping now.'


class Lion(Animal):
    pass


class Tiger(Animal):
    pass


class Cheetah(Animal):
    pass


lion = Lion('Kitty')
print(lion.name)
