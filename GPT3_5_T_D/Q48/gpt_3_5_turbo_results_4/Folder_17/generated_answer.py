
def return_binary_or_hexa(nums):
    a = nums[73]
    b = nums[84]
    
    sum = 0
    for i in range(a + 1, b):
        if i not in nums[73:85]:
            sum += i
    
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper() if sum > 0 else ""
