''' Comprehension
    (1) What is comprehension & list comprehension
    (2) set and dictionary comprehension
'''

print("===== What is comprehension & list comprehension =====")

# Comprehension acts like spread(...) operator

''' Comprehension general syntax:
    (a) *iterable object
    (b) <expression> for item in iterable
    (c) <expression> for item in iterable <condition>
'''

# list
numbers = [1, 34, 5, 67, 4, 3]
list_numbers = [*numbers]  # a version
print(list_numbers)  # comprehension mantig'i numbers list ning qiymatidan foydalanib butunlay yangi reference ga ega bo'lgan list hosil qilishda ishlatdik
print(numbers is list_numbers)
print(id(numbers), id(list_numbers))


print("-----")
people = [("Robert", 21), ("Steve", 19), ("Mike", 32)]

list_people = [person[0] for person in people]  # b version
print("list_people:", list_people)

cars = [
    ("Ferrari", 78),
    ("Toyota", 87),
    ("Audi", 116),
    ("BMW", 106),
    ("Pagani", 33),
]
list_cars = [car[0] for car in cars if car[1] > 80]
print("list_cars:", list_cars)
