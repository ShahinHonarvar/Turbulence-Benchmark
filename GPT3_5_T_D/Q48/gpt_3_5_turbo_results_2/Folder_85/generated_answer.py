
def return_binary_or_hexa(nums):
    a = nums[1]
    b = nums[8]
    s = set(nums[2:8])
    result = 0
    for i in range(a+1, b):
        if i not in s:
            result += i
    if result == 0:
        return ''
    elif result % 2 == 1:
        return bin(result)[2:]
    else:
        return hex(result)[2:].upper()
