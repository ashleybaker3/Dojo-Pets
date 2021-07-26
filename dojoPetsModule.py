class Pet:

    def __init__(self, name, type, tricks, health, energy):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy
        
    def sleep(self):
        self.energy += 25
        print(self.energy)

    def eat(self):
        self.energy += 5
        self.health += 10
        print(self.energy)
        print(self.health)

    def play(self):
        self.health += 5

    def noise(self):
        if (self.type == "dog"):
            print("woof")
        elif (self.type == "cat"):
            print("meow")