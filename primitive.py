print("===== NUMBER ======")

# In Java, variable is a name of storage location
# In Python, Variable is named reference!

count = 100
count_type = type(count)
print(f"count: {count} and type: {count_type}")

result1 = count.bit_count() # method
result2 = count.numerator # state
print(result1, result2)


print("===== STRING ======")
# METHODS: title() upper() lower() find() replace()

course = "AI Python FullStack"
result = type(course)
print(f"the result (1): {result}") 

result = course.title()
print(f"the result (2): {result}")

result = course.upper()
print(f"the result (3): {result}")

result = course.replace("FullStack", "Masterclass")
print(f"the result (4): {result}")
print(course)


print("===== BOOLEAN ======")

# functions > type() input() bool() int() str()

y = input("Give your value for y: ")
print(y)

result = y.isnumeric()
print(f"input value is numeric: {result}")

# TRUTHY vs FALSY value
# TRUTY: True 100 -100 "str"
# FALSY: False 0 "" None

test_falsy = "" or False or 0 or None
print("The FALSY: ", bool(test_falsy))

test_truthy = "str"
print("The TRUTHY: ", bool(test_truthy))
