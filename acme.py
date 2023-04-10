import random


class Product:
    '''This class contains a product'''

    def __init__(self, name, price=10, weight=20, flammability=0.5,
                 identifier=random.randint(1000000, 9999999)):
        '''this class lists the variables'''

        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        '''this function measures stealability'''

        if self.price/self.weight < 0.5:
            return "Not so stealable..."
        elif self.price/self.weight >= 0.5 and self.price/self.weight < 1.0:
            return "Kinda stealable."
        else:
            return "Very stealable!"

    def explode(self):
        '''this function measures the explosiveness'''

        if self.flammability*self.weight < 10:
            return "...fizzle."
        elif 50 > self.flammability*self.weight >= 10:
            return "...boom!"
        else:
            return "...BABOOM!!"


# Boxing Glove
class BoxingGlove(Product):
    '''This is the child class of Product'''

    def __init__(self, name, price=10, weight=10, flammability=0.5,
                 identifier=random.randint(1000000, 9999999)):
        super().__init__(name, price, weight, flammability, identifier)

    def explode(self):
        return "...it's a glove."

    def punch(self):
        '''This function returns a punch'''
        if self.weight < 5:
            return "That tickles."
        elif self.weight >= 5 and self.weight < 15:
            return "Hey that hurt!"
        else:
            return "OUCH!"
