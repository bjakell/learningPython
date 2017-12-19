#!/usr/bin/env python3.6
import os
import sys
import random

class RandomGenerator:
    def __init__(self, upper, fileName):
        self.upper = upper
        self.fileName = fileName
        randomList = []

    def writeNumbers(self):
        print(randomList + os.linesep)

    def genRandomNumber(self):
        for x in range(1, self.upper):
            randomList = randomList.append(x)

decision = input('Would you like a random number? ')

while(decision == "yes"):
    upper = int(input('Please enter the max value you want the random number to be: '))
    fileName = input('Which file would you like it written to? ')
    number = RandomGenerator(upper, fileName)
    number.genRandomNumber()
    number.writeNumbers()

    decision = input('Would you like another random number? ')

print("Well that was fun!")
