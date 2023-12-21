
def return_binary_or_hexa(nums):
    a = nums[44]
    b = nums[91]
    total_sum = sum(nums[a+1:b])
    missing_nums = [num for num in range(a+1, b) if num not in nums]
    
    if len(missing_nums) == 0:
        return ""
    
    if total_sum % 2 == 1:
        return format(total_sum, 'b')
    else:
        return format(total_sum, 'x')
