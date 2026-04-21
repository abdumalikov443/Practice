''' CLASS deep dive
    (1) ENCAPSULATION
    (2) INHERITENCE
    (3) PLOYMORPHISM
'''

print("===== ENCAPSULATION =====")

# ENCAPSULATION --> public  __private   _protected


class Account():
    # state
    description = "This class makes bank account"

    # constructor
    def __init__(self, owner, amount):
        self.__owner = owner
        self._amount = amount

    # method
    def get_balance(self):
        print(f"The owner {self.__owner} has {self._amount} usd")

    def deposit(self, amount):
        print("deposit:", amount)
        self._amount += amount

    def withdraw(self, amount):
        print("withdraw:", amount)
        self._amount -= amount

    @property 
    def holder(self): # state | objectni ichidagi maxfiy data larni olib beradi 
        return self.__owner
    
    @holder.setter
    def holder(self, new_owner):
        print("holder.setter:", new_owner)
        self._owner = new_owner

    def change_ownership(self, new_owner):
        print("change_ownership:", new_owner)
        self.__owner = new_owner

my_acc = Account("Andrew", 100)
my_acc.get_balance()

print("-------")

# getter & setter
print("owner before:", my_acc.holder) # state
my_acc.holder = "Mike" # state shaklida ishlatiladi 
print("owner after: ", my_acc.holder)


# my_acc.deposit(300)
# my_acc.withdraw(399)
# my_acc.get_balance()

# print('------------------')

# my_acc.deposit(3000)
# my_acc.get_balance()

# print('------------------')

# try:
#     r = my_acc._amount
#     print("result: ", r)
# except Exception as err:
#     print("No target state found:", err)

