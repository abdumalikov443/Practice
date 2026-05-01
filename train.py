''' G-TASK (PYTHON)

    ⭐ Savol: Shunday function tuzingki unga integerlardan iborat array pass bolsin 
    va function bizga osha arrayning eng katta qiymatiga tegishli birinchi indexni qaytarsin.
    MASALAN: get_highest_index([5, 21, 12, 21, 8]) return qiladi 1 sonini.
'''

''' Masalaning yechimi: '''
def max_num_index(arr):
    max_num = arr[0]
    for num in arr:
        if num > max_num:
            # print(num)
            max_num = num
    return arr.index(max_num)

result = max_num_index([5, 21, 12, 21, 56, 8, 43])
print(f"The highest number of index is: {result}")