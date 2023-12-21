
def return_binary_or_hexa(nums):
    a = nums[27]
    b = nums[96]
    total_sum = 0
    
    for i in range(a + 1, b):
        if i not in nums[27:97]:
            total_sum += i
    
    if total_sum % 2 == 0:
        return hex(total_sum)[2:]
    else:
        return bin(total_sum)[2:]
