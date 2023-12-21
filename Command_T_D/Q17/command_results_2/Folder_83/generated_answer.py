
def all_ints_div_by_both_two_nums(nums):
    result = []
    for i in range(90, 200):
        if nums[i] % 13 == 0 and nums[i] % -31 == 0:
            result.append(i)
    return result
