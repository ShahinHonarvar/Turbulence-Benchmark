
def return_binary_or_hexa(nums):
    a = nums[48]
    b = nums[76]
    total_sum = 0
    
    for i in range(a+1, b):
        if i not in nums[49:76]:
            total_sum += i
    
    if total_sum == 0:
        return ""
    
    if total_sum % 2 == 0:
        return hex(total_sum)[2:]
    else:
        return bin(total_sum)[2:]
