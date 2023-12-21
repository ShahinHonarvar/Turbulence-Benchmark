
def return_binary_or_hexa(nums):
    if len(nums) < 201 or len(nums) < 61:
        raise ValueError("The tuple length is too short")
    
    a, b = nums[60], nums[200]
    excluded_nums = set(range(a + 1, b)) - set(nums[61:200])
    
    total = sum(excluded_nums)
    
    if total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]
    
    return ''
