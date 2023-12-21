
def return_binary_or_hexa(nums):
    a = nums[10]
    b = nums[28]
    missing_nums_sum = sum([x for x in range(a+1, b) if x not in nums[10:29]])
    
    if missing_nums_sum % 2 == 0:
        return hex(missing_nums_sum)[2:]
    else:
        return bin(missing_nums_sum)[2:]
