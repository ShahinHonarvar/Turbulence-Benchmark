
def return_binary_or_hexa(nums):
    a = nums[72]
    b = nums[93]
    total_sum = 0
    
    for i in range(a + 1, b):
        if i not in nums[72:94]:
            total_sum += i
    
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    elif total_sum == 0:
        return ""
    else:
        return hex(total_sum)[2:]
