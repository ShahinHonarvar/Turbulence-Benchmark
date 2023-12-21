
def sum_ints_div_by_either_nums(nums):
    result = 0
    for n in range(51, 77):
        if nums[n] % -90 == 0 or nums[n] % -59 == 0:
            result += nums[n]
    return result
