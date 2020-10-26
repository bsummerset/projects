class Pet: #define class Pet
    #define the instance and include the attributes
    def __init__ (self, name, fullness = 50, happiness = 50, hunger = 5, mopiness = 5): #define instance and add attributes
       #define additional parameters for  __init__ and using values for the instance's attributes
        self.name = name
        self.fullness = fullness
        self.happiness = happiness
        self.hunger = hunger
        self.mopiness = mopiness
        self.toys = []
#define new methods with first parameter being self. This is how the body of the methods gain access to the instance and modifies its attributes.
    def eat_food(self):
        self.fullness += 30

    def get_love(self):
        self.happiness += 30

    def be_alive(self, hunger, mopiness): #implemented this method so it decrements a certain amount of fullness and happiness.
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


class CuddlyPet(Pet): #Define subclass CuddlyPet within the Pet class. 
    def __init__(self, name, fullness=50, hunger = 5, cuddle_level=1, mopiness =20):
        #Using the built-in key super() function to access Pet:
        super().__init__(name, fullness,50 , hunger, mopiness)
        self.cuddle_level = cuddle_level

    def be_alive(self):
        self.fullness -= self.hunger
        self.happiness -= self.mopiness/2


    def cuddle(self,other_pet): #define a new method called cuddle
        for i in range(self.cuddle_level):
            other_pet.get_love()
