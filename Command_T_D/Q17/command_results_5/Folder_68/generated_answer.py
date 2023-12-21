
def all_ints_div_by_both_two_nums(nums):
    result = []
    for i in range(7, len(nums), 2):
        if (i % 5 == 0 and i % 7 == 0):
            result.append(nums[i])
    return result
