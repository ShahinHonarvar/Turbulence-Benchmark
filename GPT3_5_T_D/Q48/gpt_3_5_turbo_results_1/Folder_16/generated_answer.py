
def return_binary_or_hexa(nums):
    a = nums[90]
    b = nums[97]
    total_sum = sum(nums[a+1:b])
    missing_nums = set(range(a+1, b)) - set(nums[a+1:b])
    
    if not missing_nums:
        return ""
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]
