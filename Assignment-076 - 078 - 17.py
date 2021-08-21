# First
import random


print(f"Random Number Between 10 And 50 =>{random.randint(10 ,50)}")


number = random.randrange(2 ,5)*2


if number % 2 == 0:
        print(f"Random Even Number Between 2 And 10 => {number}")


number2 = random.randrange(1, 5)*2 +1


if number2 % 2 != 0:
        print(f"Random Odd Number Between 1 And 9 => {number2}")


print("=" *50)

#Second
from My_Mod import say_Welcome, say_hello

import My_Mod

say_hello("Ali")
say_Welcome("Ali")


print("=" *50)

#Third

from My_Mod import say_hello 


say_hello("ali")


print("=" *50)

#Fourth
from My_Mod import say_Welcome as new_welcome


new_welcome("Ali")
