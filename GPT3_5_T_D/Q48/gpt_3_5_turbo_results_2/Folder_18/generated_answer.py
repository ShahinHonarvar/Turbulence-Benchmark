
def return_binary_or_hexa(nums):
    a = nums[56]
    b = nums[90]
    
    missing_nums = []
    for i in range(a + 1, b):
        if i not in nums[56:90]:
            missing_nums.append(i)
    
    if not missing_nums:
        return ""
    
    sum_missing_nums = sum(missing_nums)
    
    if sum_missing_nums % 2 == 1:
        return bin(sum_missing_nums)[2:]
    else:
        return hex(sum_missing_nums)[2:]
