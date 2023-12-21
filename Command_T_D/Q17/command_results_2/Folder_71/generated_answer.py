
def all_ints_div_by_both_two_nums(nums):
    result = []
    for i in range(68, 99 + 1):
        if nums[i] % -37 == 0 and nums[i] % -26 == 0:
            result.append(i)
    return result
