
def sum_ints_div_by_either_nums(nums):
    total = 0
    for i in range(20, 94):
        if nums[i] % -92 == 0 or nums[i] % -50 == 0:
            total += nums[i]
    return total
