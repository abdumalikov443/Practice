''' K-TASK (PYTHON)

    ⭐ Savol: Shunday function yozing, u string qabul qilsin va 
    string ichidagi eng uzun sozni qaytarsin.
    MASALAN: find_longest("I come from Uzbekistan") return "Uzbekistan" 
'''

''' Masalaning yechimi '''
def find_longest(str):
    word = ""
    
    for item in str.split():
        if len(item) > len(word):
            word = item
    return word

result = find_longest("I come from Uzbekistan") 
print(f'The result: {result}')


''' I-TASK (PYTHON)

    ⭐ Savol: Shunday function tuzing, unga string argument pass bolsin. 
    Function ushbu agrumentdagi digitlarni yangi stringda return qilsin
    MASALAN: get_digits("m14i1t") return qiladi "141"
'''

''' Masalaning yechimi '''
# def get_digits(str):
#     nums = []
#     for i in str:
#         if '0' < i < '9':
#             nums.append(i)
#     return ''.join(nums)


# result = get_digits("m14i1t") 
# print(f'The result: {result}')



''' G-TASK (PYTHON)

    ⭐ Savol: Shunday function tuzingki unga integerlardan iborat array pass bolsin 
    va function bizga osha arrayning eng katta qiymatiga tegishli birinchi indexni qaytarsin.
    MASALAN: get_highest_index([5, 21, 12, 21, 8]) return qiladi 1 sonini.
'''

''' Masalaning yechimi: '''
# def max_num_index(arr):
#     max_num = arr[0]
#     for num in arr:
#         if num > max_num:
#             # print(num)
#             max_num = num
#     return arr.index(max_num)

# result = max_num_index([5, 21, 12, 21, 56, 8, 43])
# print(f"The highest number of index is: {result}")