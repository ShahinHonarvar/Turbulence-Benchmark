
def all_ints_div_by_both_two_nums(nums):
    result = []
    for i in range(0, 7):
        x = nums[i]
        if x % -5 == 0 and x % -6 == 0:
            result.append(x)
    return result
