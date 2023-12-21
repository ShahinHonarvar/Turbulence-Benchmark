
def return_binary_or_hexa(nums):
    a = nums[200]
    b = nums[202]
    
    missing_nums = []
    for i in range(a+1, b):
        if i not in nums[200:203]:
            missing_nums.append(i)
    
    if len(missing_nums) == 0:
        return ""
    
    sum_missing_nums = sum(missing_nums)
    
    if sum_missing_nums % 2 == 1:
        return bin(sum_missing_nums)[2:]
    else:
        return hex(sum_missing_nums)[2:]
