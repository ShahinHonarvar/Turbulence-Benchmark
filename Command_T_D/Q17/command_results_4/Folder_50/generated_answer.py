
def all_ints_div_by_both_two_nums(nums):
    result = []
    for x in range(46, 91):
        if nums[x] % 67 == 0 and nums[x] % 15 == 0:
            result.append(x)
    return result
