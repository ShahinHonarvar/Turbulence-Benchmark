
def return_binary_or_hexa(nums):
    a = nums[56]
    b = nums[90]
    sum = 0
    for i in range(a+1, b):
        if i not in nums[56:91]:
            sum += i
    if sum == 0:
        return ""
    elif sum % 2 == 0:
        return hex(sum)[2:].upper()
    else:
        return bin(sum)[2:]
