
def return_binary_or_hexa(nums):
    a = nums[22]
    b = nums[24]
    total = 0
    
    for i in range(a + 1, b):
        if i not in nums[23:24]:
            total += i
    
    if total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]
