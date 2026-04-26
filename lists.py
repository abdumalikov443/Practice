''' LIST
    (1) Working with lists
    (2) List methods
    (3) Lambda function
    (4) Enumerate, map & filter
'''

print("===== Working with lists =====")
# Java / PHP / NodeJS array => Python list

# literal
person = {"name": "Andrew", "age": 20}  # dictionary
people = ("Andrew", "John", "Michael")  # tuple
groups = ["MIT", "FLEXY", "DEVEX", "MG"]  # list

for team in groups:
    print("the team:", team)


# constructor
letters = list("Hello World!")
print(f"the letters: {letters} and size: {len(letters)}")

print("-----")

fruits = ["grape", "apple", "melon", "kiwi", "cherry", "orange"]

a = fruits[0]
b = fruits[0:2]
c = fruits[3::2]
d = fruits[5::-2]

print("a: {}, b: {}, c: {}, d: {}".format(a, b, c, d))

print("\n===== List methods =====")
# methods --> append() insert() pop() remove() clear() sort() => mutable |  index() => immutable

letters = ["a", "b", "d"]

letters.append("c")  # add element to end
print(f"append letters: {letters}")

letters.insert(2, "z")  # add element to before the value at 0 index
print(f"insert letters: {letters}")

size = len(letters) - 1

r1 = letters.pop(size)  # pop behind
print(f"the pop result1: {r1} and letters: {letters}")

r2 = letters.pop(0)  # pop front
print(f"the pop result2: {r2} and letters: {letters}")


print("------")

animals = ["fish", "cat", "dog", "lion", "tiger"]
print("animals:", animals)

animals.remove("dog")
print("remove animals:", animals)

del animals[2:4]
print("del animals:", animals)

exist = animals.index("cat")
print("cat exists:", exist)

# animals.clear()
# print("animals: ", animals)

if "cat" in animals:
    print("index of cat:", animals.index("cat"))
else:
    print("cat does not exist")


print("------")

numbers = [2, 12, 8, 5, 34, 23]

numbers.sort()
print("sort default:", numbers)
numbers.sort(reverse=True)
print("sort reverse:", numbers)

# immutable --> sorted function & index method
numbs = [34, 756, 1, 2]
new_nums = sorted(numbs)
print(f"numbs: {numbs} and new_nums: {new_nums}")


print("\n===== Lambda function =====")
# lambda is small anonymous function!

def calculate(x, y): return x * y

result = calculate(3, 5)
print("result:", result)

# lambdaning asosiy kuchi > ikkala valueni ham alohida chiqarib beradi
people = [
    ("Robert", 20),
    ("Steve", 4),
    ("Joseph", 25),
    ("Michael", 1),
    ("Ali", 40)
]  

people.sort()
print("people1:", people)

# sort by age via lambda function
people.sort(key = lambda person: person[1])
print("people2:", people)

