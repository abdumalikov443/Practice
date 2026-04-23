''' LOOP operators
    (1) for
    (2) break / else
    (3) while
'''

print("===== for operator =====")
# Iterable objects > string dict tuple list range map filter

text = "MIT"
nums = [12, 4, 7, 3]
car_object = dict(brand="Range Rover", year=2025)
range_object = range(8)  # [0, 8)

for char in text:
    print(f"the character: {char}")

print("-----")
for n in nums:
    print(f"the number: {n}")

print("-----")
for key in car_object:
    print(f" The key: {key} => it's value: {car_object.get(key)}")


print("===== break / else =====")
for x in range(1, 20, 3):
    print(f" the x: {x}")
    if x > 10:
        print("You reached break")
        break
else:       # agar  for ni ichidagi shart(if) bajarilmasa else ishga tushadi oxirida
    print("Looped successfully") 


print("===== whie operator =====")
num = 38
while num < 50:
    num += 8
    print(f"The num equals to {num}")

print("-----")
count = 0
while True:
    count += 1
    x = int(input("Predict the number: "))

    if x == 41:
        print(f"You found the number in {count} steps")
        break
    else:
        print("Wrong number, please try again!")


# Xulosa: For qachonki step(urunishlar) soni aniq bo'lsa ishlatiladi, while esa urunishlar soni noma'lum bo'lganda ishlatiladi