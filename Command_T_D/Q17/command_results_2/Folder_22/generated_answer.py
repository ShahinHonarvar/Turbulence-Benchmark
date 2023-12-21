
def all_ints_div_by_both_two_nums(nums):
    result = []
    for i in range(40, 200):
        if nums[i] % 21 == 0 and nums[i] % 71 == 0:
            result.append(nums[i])
    return result
