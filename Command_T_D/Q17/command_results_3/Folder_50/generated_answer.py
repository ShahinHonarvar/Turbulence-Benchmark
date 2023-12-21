
def all_ints_div_by_both_two_nums(nums):
    result = []
    for i in range(46, 91+1):
        if nums[i] % 67 == 0 and nums[i] % 15 == 0:
            result.append(nums[i])
    return result
