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