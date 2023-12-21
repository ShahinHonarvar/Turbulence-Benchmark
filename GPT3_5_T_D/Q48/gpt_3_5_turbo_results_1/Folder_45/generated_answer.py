
def return_binary_or_hexa(nums):
    a = nums[30]
    b = nums[200]
    total = 0
    for i in range(a + 1, b):
        if i not in nums[30:200]:
            total += i
    
    if total % 2 == 0:
        return hex(total)[2:].upper()
    else:
        return bin(total)[2:]
