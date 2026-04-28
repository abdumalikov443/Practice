''' Comprehension
    (1) What is comprehension & list comprehension
    (2) Set and Dictionary comprehension
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
list_cars = [car[0] for car in cars if car[1] > 80]  # c version
print("list_cars:", list_cars)


print("\n===== Set and dictionary comprehension =====")
nums = [1, 4, 5, 9, 1, 4, 7, 5, 3]
set_nums = {*nums}
print("set_nums:", set_nums)


dict_people = {person[0]: person[1] for person in people}  # a version
print("dict_people:", dict_people)

dict_people2 = {person[0]: person[1] for person in people if person[1] > 20}  # b version
print("dict_people 2:", dict_people2)

# (<expression> for item in iterable) generic type -->  katta hajmdagi ma'lumotlar to'plamini hosil qilish uchun ishlatiladi