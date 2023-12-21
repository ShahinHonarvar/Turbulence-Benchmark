
def return_binary_or_hexa(nums):
    a = nums[13]
    b = nums[91]
    
    missing_nums = set(range(a + 1, b)) - set(nums[13:91])
    
    sum_missing = sum(missing_nums)
    
    if sum_missing % 2 == 0:
        return hex(sum_missing)[2:].upper() if sum_missing != 0 else ""
    else:
        return bin(sum_missing)[2:] if sum_missing != 0 else ""
