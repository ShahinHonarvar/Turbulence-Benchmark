
def return_binary_or_hexa(nums):
    a = nums[57]
    b = nums[85]
    sum = 0
    for i in range(a+1, b):
        if i not in nums[58:85]:
            sum += i
    
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]
