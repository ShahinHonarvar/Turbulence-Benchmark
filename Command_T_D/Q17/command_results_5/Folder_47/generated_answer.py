
def all_ints_div_by_both_two_nums(nums):
    result = []
    for i in range(42, 87):
        if nums[i] % -90 == 0 and nums[i] % -74 == 0:
            result.append(i)
    return result
