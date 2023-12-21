
def all_ints_div_by_both_two_nums(nums):
    result = []
    for i in range(828, 932):
        if nums[i] % -649 == 0 and nums[i] % -461 == 0:
            result.append(i)
    return result
