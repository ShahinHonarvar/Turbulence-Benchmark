
def return_binary_or_hexa(nums):
    a = nums[6]
    b = nums[9]
    total = 0
    
    for i in range(a + 1, b):
        if i not in nums[6:9]:
            total += i
            
    if total == 0 or total % 2 == 0:
        return hex(total).lstrip("0x")
    else:
        return bin(total).lstrip("0b")
