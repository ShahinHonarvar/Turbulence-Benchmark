
def sum_ints_div_by_either_nums(nums):
    for i in range(40, 200):
        if nums[i] % 21 == 0 or nums[i] % 71 == 0:
            return nums[i]
    return 0
