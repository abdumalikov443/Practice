''' Array &SEt
    (1) Array
    (2) Set
    (3) Specific operators with set
'''

from array import array

print("===== Array =====")

# arrayni faqatgina juda zarur bo'lgan vaqtda qachonki sonlarimiz ketma-ketligi judayam ko'p bo'lganda ishlatamiz
numbers = array("i", [1, 4, 6, 27, 6, 83, 7, 32])
print("numbers1: ", numbers)

numbers.append(100) # oxiridan qo'shadi
numbers.insert(0, 123) # index ga qo'shadi
print("numbers2: ", numbers)

numbers.remove(6) # value ni o'chirad
numbers.pop() # oxirgi elementni o'chiradi
print("numbers3: ", numbers)

del numbers[2:4]
print("numbers4: ", numbers)