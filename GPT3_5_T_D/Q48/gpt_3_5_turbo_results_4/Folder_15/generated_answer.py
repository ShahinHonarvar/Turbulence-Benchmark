
def return_binary_or_hexa(nums):
    a = nums[0]
    b = nums[4]
    missing_nums = [x for x in range(a + 1, b) if x not in nums[1:4]]
    sum_missing_nums = sum(missing_nums)
    
    if sum_missing_nums == 0:
        return ""
    elif sum_missing_nums % 2 == 1:
        return bin(sum_missing_nums)[2:]
    else:
        return hex(sum_missing_nums)[2:].upper()
