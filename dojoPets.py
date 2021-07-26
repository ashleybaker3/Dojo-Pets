import dojoPetsModule

class Ninja:

    def __init__(self, first_name , last_name , treats , pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        self.pet.play()
        print(self.pet.health)
        # leaving the print here to show that there are two ways to print! Either by walking to the attribute through this function or doing it in the other function that is called

    def feed(self):
        self.pet.eat()

    def bathe(self):
        self.pet.noise()

    # walk() - walks the ninja's pet invoking the pet play() method
    # feed() - feeds the ninja's pet invoking the pet eat() method
    # bathe() - cleans the ninja's pet invoking the pet noise() method




Masha = dojoPetsModule.Pet("Masha", "cat", "Dance", 10, 10)
Ichigo = Ninja("Ichigo", "Momomiya", 20, 30, Masha)

Ichigo.walk()
Ichigo.feed()
Ichigo.bathe()



