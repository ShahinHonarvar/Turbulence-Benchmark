
def all_ints_div_by_both_two_nums(nums):
    result = []
    for i in range(29, 53):
        x = nums[i]
        if x % -68 == 0 and x % -85 == 0:
            result.append(x)
    return result
