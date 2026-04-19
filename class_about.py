''' CLASS
    (1) What is class?
    (2) ordinary & static properties
    (3) special methods
'''

print("====== What is class ======")
# class - blueprint for object creation!
# structure -> state constructor method


class Person():
    # state
    # objectga boglanmagan va class bn birga keladigan static state hisoblanadi
    message = "static state property"

    # constructor
    def __init__(self, name, age):  # self--> person classdan yaratilgan object ga qaratilgan
        self.name = name
        self.age = age

    # method
    def introduce(self):
        print(f'{self.name} says: How do you do?')

    def say_age(self):
        print(f'{self.name} says I am {self.age} y.o')

    @classmethod
    def explain(cls):
        print("Static method property executed")


person1 = Person("Andrew", 20)
person2 = Person("Mike", 24)
person3 = Person("Tom", 12)


# ordinary state
print(f"person1.name: {person1.name}")

# ordinary method
person1.introduce()
person2.say_age()


print("\n====== ordinary & static properties ======")
# static state
new_message = Person.message
print(f"result: {new_message}")

# static method
Person.explain()


print("\n====== special | magic methods ======")
# Python's most common special methods are below:
# __str__ __init__ __len__ __new__ __call__ __getitem__ ...


class Car():
    # state
    description = "This class makes cars"

    # contructor
    def __new__(cls, *args):
        print("* __new__ *")
        return super().__new__(cls)

    def __init__(self, name, year):
        self.name = name
        self.year = year

    # method

    def start_engine(self):
        print(f"The {self.name} started engine!")

    def stop_egine(self):
        print(f"The {self.name} stopped engine!")

    def __str__(self):
        return f"The {self.name} was produced in {self.year} year!"

    def __call__(self):
        print("object called as a function")
        return True


my_car = Car("Porsche", 2025)
my_car.start_engine()
my_car.stop_egine()

print('------')
m_car = Car("Dodge", 2023)
print(m_car)
r = m_car()  # look like a function
print("Result:", r)
