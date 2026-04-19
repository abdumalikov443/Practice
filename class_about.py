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
    message = "static state property"  # objectga boglanmagan va class bn birga keladigan static state hisoblanadi

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