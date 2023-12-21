
def return_binary_or_hexa(nums):
    a = nums[15]
    b = nums[57]
    total = 0
    
    for i in range(a+1, b):
        if i not in nums[15:58]:
            total += i
    
    if total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]
