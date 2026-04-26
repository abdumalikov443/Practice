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

numbers.append(100)  # oxiridan qo'shadi
numbers.insert(0, 123)  # index ga qo'shadi
print("numbers2: ", numbers)

numbers.remove(6)  # value ni o'chirad
numbers.pop()  # oxirgi elementni o'chiradi
print("numbers3: ", numbers)

del numbers[2:4]
print("numbers4: ", numbers)

print("\n===== Set =====")
# { set } is a unique collection without keeping order!

new_numbers = array("i", [1, 4, 6, 27, 6, 4, 1, 83])
num_set = set(new_numbers)

print("num_set: ", num_set, type(num_set))

num_set.add(200)
print(num_set)

num_set.add(6)
print(num_set)

print("===== Specific operators with set =====")
# | & - ^

a = {10, 30, 42}
b = {15, 42, 83}

result1 = a | b  # union --> 2 ta to'plamdagi qiymatlarni setga joylab takrorlanganlarni 1 tasini yozadi holos

result2 = a & b  # intersection --> ikkovida ham bor bo'lgan qiymatni qaytaradi

result3 = a - b  # difference -->  a dan b ni ayrib beradi, va faqat a ni natijasini qaytaradi

result4 = a ^ b # symmetric difference --> 2 ta to'plam orasida bir-birida yo'q bo'lgan qiymatni qaytaradi 

print("result1:", result1)
print("result2:", result2)
print("result3:", result3)
print("result4:", result4)
