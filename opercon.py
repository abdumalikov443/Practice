''' OPERATORS & CONDITIONS
    (1) Operators
    (2) Condition
    (3) Logical Operators
'''

print("===== Operators =====")
# + - > < >= <= == is * /  // % += **

a = 19
b = 5

# print("a > b", a > b)
# print("a / b", a / b)

result = a // b
left = a % b
print(f"The result: {result} and left: {left}")

a += 100
print("a:", a)

print("a ** b", a ** b)
print("=" * 12)

c = dict(name="Sam", age=23)
d = dict(name="sam", age=23)
print("result:", c == d)  # only value compares
print(id(c), id(d))

data = c is d  # c d objectmi | reference lar solishtirilyapti
print(data)


print("===== Conditions =====")

x = 15
if x > 50:
    print("Case A")
elif x > 10:
    print("Case B")
else:
    print("Case C")

print("===== Logical Operators =====")

age = 20
# person = None

# if age > 18:
#     person = "Adult"
# else:
#     person = "minor"
# print("person:", person)

# Ternary operator
person = "Adult" if age > 18 else "minor"
print("person:", person)

print("-"*12)

is_student = False
is_admin = True
is_guest = False
is_parent = False

if not is_student:
    print("Wellcome here, do you want to be a student?")
elif is_admin:
    print("please go to that office")
elif is_guest or is_parent:
    print("Waiting room is over there!")
else:
    print("Other cases")
