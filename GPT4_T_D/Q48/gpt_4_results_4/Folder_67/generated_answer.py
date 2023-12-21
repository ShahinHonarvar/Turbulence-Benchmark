
def return_binary_or_hexa(nums):
    a = nums[44]
    b = nums[67]
    missing_nums = set(range(a + 1, b)) - set(nums[44:68])
    sum_nums = sum(missing_nums)
    if sum_nums == 0:
        return ""
    elif sum_nums % 2 == 0:
        return hex(sum_nums)[2:].upper() 
    else:
        return bin(sum_nums)[2:]
