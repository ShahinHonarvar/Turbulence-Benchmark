
def all_ints_div_by_both_two_nums(nums):
    result = []
    for i in range(0, 4):
        x = nums[i]
        if x % 11 == 0 and x % -7 == 0:
            result.append(x)
    return result
