
def sum_ints_div_by_either_nums(nums):
    for i in range(90, 97):
        if nums[i] % 13 == 0 or nums[i] % 35 == 0:
            return nums[i]
    return 0
