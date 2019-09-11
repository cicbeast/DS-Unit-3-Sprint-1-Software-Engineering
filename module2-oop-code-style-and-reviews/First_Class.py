'''
DSPT1 Unit 3 Sprint 1 Module 2-OOP and Code Style
'''
from random import randint


class TwentySided:
    '''General Representation of a 20 Sided Die'''

    def __init__(self, color='white', sides=20, p1='Raul', p2='Chris'):
        self.rolls = 1
        self.player1 = p1
        self.player2 = p2

    def list_players(self):
        '''Prints the rollers of the die'''
        print('{} is rolling first, and {} is rolling second'.format(self.player1, self.player2))

    def roll_die(self):
        '''Rolling the 20 Sided Die'''
        self.roll1 = randint(1,20)
        self.roll2 = randint(1,20)
    
    def print_results(self):
        '''Prints the results of the Roll'''
        print('{} rolled a {}, while {} rolled a {}'.format(self.player1, self.roll1, self.player2, self.roll2))
        if self.roll1 > self.roll2: print('{} Wins!'.format(self.player1))
        elif self.roll2 > self.roll1: print('{} Wins!'.format(self.player2))
        else: print("It's a TIE!!")



