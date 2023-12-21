
def return_binary_or_hexa(nums):
    a = nums[13]
    b = nums[70]
    total = 0
    
    for i in range(a + 1, b):
        if i not in nums[13:71]:
            total += i
    
    if total == 0:
        return ""
    elif total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]
