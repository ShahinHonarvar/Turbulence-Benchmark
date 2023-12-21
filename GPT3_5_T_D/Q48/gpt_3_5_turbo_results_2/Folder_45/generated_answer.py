
def return_binary_or_hexa(nums):
    a = nums[30]
    b = nums[200]
    
    missing_nums = [x for x in range(a+1, b) if x not in nums[30:201]]
    if len(missing_nums) == 0:
        return ""
    
    sum_missing = sum(missing_nums)
    
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]
