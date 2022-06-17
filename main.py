#****************************************************************
#Name:GOODNEWS AGBADU

#
#ANA1001 Lab 3
#****************************************************************



#Dice class. Use the random module to generate random numbers using randint(). Make a class named Die with one attribute called sides which has a default value of 6. Write a method called roll_die() that prints out a random number between 1 and the number of sides the die has.

from random import randint

class Die():
    """Represent a die, which can be rolled."""

    def __init__(self, sides):
        """Initialize the die."""
        self.sides = sides

    def roll_die(self):
        """Return a number between 1 and the number of sides."""
        return randint(1, self.sides)

#a.Make a 6 sided die instance and roll it ten times, store the results in a list and print it out

die_six = Die(sides=6)
#store the results
results = []
for rollnum in range(10):
    result = die_six.roll_die()
    results.append(result)
print("10 rolls of a 6-sided die:")
print(results)

#b. Make a 10 sided die and roll it 20 times, store the results in a list and print it out
die_ten = Die(sides=10)
#store the results
results = []
for rollnum in range(20):
    result = die_ten.roll_die()
    results.append(result)
print("\n20 rolls of a 10-sided die:")
print(results)

# c. Make a 20 sided die and roll it 20 times, store the results in a list and print it out
die_twenty = Die(sides=20)
#store the results
results = []
for rollnum in range(10):
    result = die_twenty.roll_die()
    results.append(result)
print("\n20 rolls of a 20-sided die:")
print(results)
print()
print()

#We are going to set up a class for a stock broker which will perform some common tasks, set up instances of clients, and enter trades. Set up a class called Stocks inside of a module called stock_company.py Inside of the module, set up at least three methods. Test your class and methods by writing code in main.py

#class stocks with three methods
from stock_company import stock

my_action =stock('sell','buy', 'wait')

my_action.stock_movement_ifrise()
my_action.stock_movement_ifdrop()
my_action.stock_movement_ifflat()