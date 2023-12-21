
def return_binary_or_hexa(nums):
    a = nums[40]
    b = nums[200]
    total = 0
    
    for i in range(a + 1, b):
        if i < a or i > b or i in nums[40:200]:
            continue
        total += i
    
    if total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]
