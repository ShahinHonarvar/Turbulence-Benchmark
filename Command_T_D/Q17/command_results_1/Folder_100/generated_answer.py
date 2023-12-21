
def all_ints_div_by_both_two_nums(nums):
    result = []
    for i in range(72, 93):
        if nums[i] % 32 == 0 and nums[i] % 44 == 0:
            result.append(nums[i])
    return result
