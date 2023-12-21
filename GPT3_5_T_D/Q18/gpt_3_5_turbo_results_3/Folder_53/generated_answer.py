
def sum_ints_div_by_either_nums(nums):
    total = 0
    for i in range(200, 201):
        if nums[i] % 17 == 0 or nums[i] % -5 == 0:
            total += nums[i]
    return total
