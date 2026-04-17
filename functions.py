''' FUNCTIONS
    (1) DEFINE vs CALL
    (2) Parameter vs Argument
    (3) Keyword & default arguments
    (4) Scope
'''

print("====== DEFINE (parameter) vs CALL (argument) =====")
# build in function > print() type()
# Function > reusable block of code
# Instead of block {} in Java, Python uses Indentation


# DEFINE - parameter
def greet(a):  # void
    print(f"How do you do, {a}?")


def greeting(b):  # return
    print("greeting is executed")
    return f"Hi {b}"


# CALL - argument
r = greet('Andrew')
print(r)

r2 = greeting('Mike')
print(r2)


print("====== Keyword & default arguments =====")
# DEFINE
def give_greet(name, age=20):
    print("give_greet is executed!")
    return f"Hi {name}, you are {age} years old"


r3 = give_greet("Andrew", 20)
print(r3)

r4 = give_greet("Andrew")
print(r4)
