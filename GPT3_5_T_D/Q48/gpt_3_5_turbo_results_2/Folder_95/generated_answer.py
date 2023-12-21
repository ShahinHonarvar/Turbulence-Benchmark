
def return_binary_or_hexa(nums):
    a = nums[32]
    b = nums[99]
    
    missing_nums = [x for x in range(a + 1, b) if x not in nums[32:100]]
    if len(missing_nums) == 0:
        return ""
    
    sum_missing_nums = sum(missing_nums)
    
    if sum_missing_nums % 2 == 1:
        return format(sum_missing_nums, 'b')
    else:
        return format(sum_missing_nums, 'X')
