
def return_binary_or_hexa(nums):
    a = nums[60]
    b = nums[200]
    
    range_sum = sum(range(a+1, b))
    missing_nums = [num for num in range(a+1, b) if num not in nums[61:200]]
    
    if not missing_nums:
        return ""
    
    if range_sum % 2 == 1:
        return bin(range_sum)[2:]
    else:
        return hex(range_sum)[2:]
