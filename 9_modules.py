'''
import math

print(math.pi)
print(math.sqrt(49))
print(math.pow(2,3))
'''

from math import sqrt
print(sqrt(25))

import random
print(random.randint(1,20))
import string
random_letter = random.choice(string.ascii_letters)
print(random_letter)

small_letters = random.choice(string.ascii_lowercase)
print(small_letters)

capital_letters = random.choice(string.ascii_uppercase)
print(capital_letters)

list1 = [1,2,3,4,5]
print(random.choice(list1))

#try out multiple random generation
#tryout secret module...eg otp

import datetime
print(datetime.datetime.now())

print(datetime.date.today())
print(datetime.date.today() - datetime.timedelta(1))
#try out random dates in btw specific dates

import sys
print(sys.platform)
print(sys.version)

import os
print(os.getcwd())
print(os.listdir())

#aliasing

import datetime as dt
print(dt.datetime.now())

import requests
url = requests.get('https://jsonplaceholder.typicode.com/users/2')
print(url.json())