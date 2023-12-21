
def all_ints_div_by_both_two_nums(nums):
    result = []
    for i in range(1, 5):
        if nums[i] % 4 == 0 and nums[i] % -6 == 0:
            result.append(nums[i])
    return result
