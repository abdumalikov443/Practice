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
print("result:", c==d) # only value compares
print(id(c), id(d))

data = c is d # c d objectmi | reference lar solishtirilyapti
print(data)