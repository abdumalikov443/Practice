''' OBJECTS 
    (1) What is object?
    (2) Iterable objects & RANGE
    (3) DICTIONARY
    (4) Error handling system
'''

import array  # package/ module
import math
from math import ceil

print("===== What is object =====")
# An object has a state and method properties
# Everything is object in Python

print(type('Hello world'))
print(type(2))
print(type(True))
print(type(array))
print(type(math))


# Paradigm: Functional Programming & OOP
# 4 OOP ONCEPTS: Abstraction - Encapsulation - Inheritence - Polymorphism
r1 = math.ceil(12.3)
print(f" \nresult1: {r1}")

r2 = math.ceil(33.73)
print(f" \nresult2: {r2}")



print("\n======= Error handling system =======")

car_dict = dict(name='Toyota', year=2024, electric=False)

try: 
    print("Passed here") # birinchi bu print bo'ladi ishlamasa err ni print qiladi
    a = car_dict.speed
    r = car_dict['year']
    print('result: ', r)
except Exception as err:
    print("Global Error: ", err)
else: 
    print("Executed succesfully without errors")
finally:
    print("Final logic")
