
def return_binary_or_hexa(nums):
    a = nums[29]
    b = nums[53]
    total_sum = sum(nums[a+1:b])
    missing_nums = set(range(a+1, b+1)) - set(nums[a+1:b])
    
    if missing_nums:
        if total_sum % 2 == 1:
            return bin(total_sum)[2:]
        else:
            return hex(total_sum)[2:]
    else:
        return ""
