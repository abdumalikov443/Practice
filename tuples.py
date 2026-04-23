''' TUPLE 
    (1) What is tuple: tuple vs list
    (2) Unpacking arguments
    (3) zip
'''

print("===== What is tuple: tuple vs list =====")
# Java/PHP/NodeJS array == Python list

# literal
nums = [1, 5, 8, 2]
print(nums)

# constructor
fruits = ["apple", "lemon", "banana", "kiwi"]
print("before fruits:", fruits)

fruits[3] = "grape"
print("after fruits: ", fruits)

# tuple --> hech qachon qiymatini o'zgartirmaydi
animals = ("dog", "cat", "fish", "bear")
tuple_object = ("MIT", 12, True, None)

print(animals[0])
# animals[0] = "bird"

# try avoid these
people = "Andrew", "John"
animals = "dog", "cat",

print("===== Unpacking arguments =====")

groups = ["MIT", "FLEXY", "DEVEX", "MG"]
(x, y, *z) = groups
print(f"the x: {x} and y: {y}")
print("z:", z)  # list

# *args > tuple


def calculate(*args):
    print("*args >", args)
    total = 1
    for x in args:
        total *= x
    print(f"the total value: {total}")
    return total


# CALL
calculate(1, 3, 6, 5)
print("-----")
calculate(0, 3, 200)
print("-----")
calculate(5, 9)

print("-----")
# **kwargs > dictionary


def introduce(**kwargs):
    print(f"the type(**kwargs) : {type(kwargs)}")
    print(f"Hi, i am {kwargs["name"]} and i am {kwargs["age"]} years old")
    pass


# CALL
introduce(name="Andrew", age=20)
introduce(name="Shawn", age=32, single=True)