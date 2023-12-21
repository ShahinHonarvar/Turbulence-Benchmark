
def all_ints_div_by_both_two_nums(nums):
    result = []
    for i in range(73, 87):
        if nums[i] % 54 == 0 and nums[i] % 82 == 0:
            result.append(nums[i])
    return result
