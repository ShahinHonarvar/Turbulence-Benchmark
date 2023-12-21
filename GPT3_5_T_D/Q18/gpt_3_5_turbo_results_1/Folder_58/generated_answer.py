
def sum_ints_div_by_either_nums(nums):
    total = 0
    for i in range(240, 902):
        if nums[i] % 546 == 0 or nums[i] % 709 == 0:
            total += nums[i]
    return total
