
def all_ints_div_by_both_two_nums(nums):
    result = []
    for i in range(25, 81):
        if nums[i] % -20 == 0 and nums[i] % -26 == 0:
            result.append(nums[i])
    return result
