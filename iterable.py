print("======= Iterable objects & RANGE =======")
# Iterable objects --> string dict tuple list range map filter


range_obj = range(5)
print(f"range_obj: {range_obj}\n")

for letter in "MIT":
    print(f"the letter: {letter}")

for ele in range_obj:
    print(f"the element: {ele}")


print("======= DICTIONARY =======")
# Dictionary is JSON objec!
person = {"name": "Andrew", "age": 20, "single": True}
person_obj = dict(name="Andrew", age=20, single=True)
print(f"the person: {person}")
print(f"The person_obj: {person_obj}")


# method: get()
# name = person_obj["name"]

name = person.get("name")
age = person_obj.get("age")
balance = person.get("balance", 0) # balance degan key bo'lmasa uni valuesi 0 bo'lib qaytadi
hobby = person_obj.get("hobby") # hobby key yo'q bo'lgani uchun None qaytaradi

print(f"\nname: {name}, age: {age} & hobby: {hobby} and balance: {balance}")

del person_obj['single']
for key in person_obj:
    print(f"the key: {key} --> value: {person_obj[key]}") # person_obj.get(key)

