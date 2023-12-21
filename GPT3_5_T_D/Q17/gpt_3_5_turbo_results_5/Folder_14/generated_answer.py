
def all_ints_div_by_both_two_nums(nums):
    result = []
    for i in range(7, 10):
        if nums[i] % 2 == 0 and nums[i] % 3 == 0:
            result.append(nums[i])
    return result
