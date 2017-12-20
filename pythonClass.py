#!/usr/bin/env python3.6
import sys
import random

class RandomGenerator:
    def __init__(self, upper, fileName):
        self.upper = upper
        self.fileName = fileName
        self.randomList = []

    def writeNumbers(self):
        #for x in self.randomList:
            #print(x)
        print(self.randomList)

    def genRandomNumber(self):
        x = random.randint(0, self.upper)
        if x not in self.randomList:
            self.randomList.append(x)

decision = input('Would you like a random number? ')
upper = int(input('Please enter the max value you want the random number to be: '))
fileName = input('Which file would you like it written to? ')
number = RandomGenerator(upper, fileName)

while(decision == "yes"):
    number.genRandomNumber()
    number.writeNumbers()
    decision = input('Would you like another random number? ')
    upper = int(input('Please enter the max value you want the random number to be: '))

print("Well that was fun!")
