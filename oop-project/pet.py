class Pet:
    def __init__ (self, name, fullness = 50, happiness = 50, hunger = 5, mopiness = 5):
        self.name = name
        self.fullness = fullness
        self.happiness = happiness
        self.hunger = hunger
        self.mopiness = mopiness
        self.toys = []

    def eat_food(self):
        self.fullness += 30

    def get_love(self):
        self.happiness += 30

    def be_alive(self, hunger, mopiness):
        self.fullness -= hunger
        self.happiness -= mopiness
        for toy in self.toys:
            self.happiness += toy.use()

    def get_toy(self, toy):
        self.toys.append(toy)


    def __str__(self):
        return """"
        %s:
        Fullness: %s
        Happiness: %s
        """ % (self.name, self.fullness, self.happiness)


class CuddlyPet(Pet):
    def __init__(self, name, fullness=50, hunger = 5, cuddle_level=1, mopiness =20):
        super().__int__(name, fullness,50 , hunger, mopiness)
        self.cuddle_level = cuddle_level

    def be_alive(self):
        self.fullness -= self.hunger
        self.happiness -= self.mopiness/2


    def cuddle(self,other_pet):
        for i in range(self.cuddle_level):
            other_pet.get_love()
