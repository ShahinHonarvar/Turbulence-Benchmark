
def sum_ints_div_by_either_nums(nums):
    result = 0
    for i in range(51, 77):
        if nums[i] % -90 == 0 or nums[i] % -59 == 0:
            result += nums[i]
    return result
