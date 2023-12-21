
def return_binary_or_hexa(nums):
    a = nums[11]
    b = nums[76]
    missing_nums = [x for x in range(a + 1, b) if x not in nums[12:76]]
    
    if len(missing_nums) == 0:
        return ""
    
    total_sum = sum(missing_nums)
    
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]
