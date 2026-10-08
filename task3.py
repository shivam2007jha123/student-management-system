import random #importing random library to generate random numbers
import math #importing math library to perform mathematical operations
import datetime #importing datetime library to display current date and time

#it generates a random number between 1 to 100
number=random.randint(1,100)
print("random number is:",number)

#it performs square root of the number
sqrt=math.sqrt(number)
print("square root of the number is:",sqrt)

#it displays the current date and time
now=datetime.datetime.now()
print("current date and time is:",now)

