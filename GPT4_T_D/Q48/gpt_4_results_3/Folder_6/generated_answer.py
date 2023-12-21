
def return_binary_or_hexa(nums):
    a, b = nums[20], nums[93]
    
    range_set = set(range(a + 1, b))
    nums_set = set(nums[21:93])
    diff = range_set - nums_set

    sum_diff = sum(diff)

    if sum_diff == 0:
        return ""
    elif sum_diff % 2 == 0:
        return hex(sum_diff)[2:].upper()
    else:
        return bin(sum_diff)[2:]
