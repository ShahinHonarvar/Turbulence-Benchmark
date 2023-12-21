
def return_binary_or_hexa(nums):
    a = nums[275]
    b = nums[871]
    
    missing_nums = [i for i in range(a + 1, b) if i not in nums[275:872]]
    
    if len(missing_nums) == 0:
        return ""
    
    sum_missing = sum(missing_nums)
    
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]
