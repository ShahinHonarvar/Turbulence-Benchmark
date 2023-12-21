
def return_binary_or_hexa(nums):
    a = nums[39]
    b = nums[43]
    
    total_sum = 0
    
    for i in range(a + 1, b):
        if i not in nums[39:44]:
            total_sum += i
    
    if total_sum == 0:
        return ""
    elif total_sum % 2 == 0:
        return format(total_sum, 'X')
    else:
        return format(total_sum, 'b')
