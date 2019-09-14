import unittest
import random

class Product():
    def __init__(self, name, price=10, weight=20, flammability=0.5, identifier=random.randint(1000000,9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier
    
    def stealability(self):
        '''Uses the quotient of price & weight to calculate how 'stealable' an product is'''
        q = self.price / self.weight
        if q < 0.5: print('Not so stealable...')
        elif 0.5 <= q < 1: print('Kinda Stealable.')
        else: print('Very Stealable')
    
    def explode(self):
        '''Uses the product of flammability & weight to calculate how likely it is that the product will blow up'''
        p = self.flammability * self.weight
        if p < 10: print('...fizzle.')
        elif 10 <= p < 50: print('...boom!')
        else: print('...BABOOM!!')

class BoxingGlove(Product):
    def __init__(self, name, price=10, weight=10, flammability=0.5, identifier=random.randint(1000000,9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def explode(self):
        print("...it's a glove.")

    def punch(self):
        if self.weight < 5: print('That Tickles.')
        elif 5 <= self.weight < 15: print('Hey that hurt!')
        else: print('OUCH!')
