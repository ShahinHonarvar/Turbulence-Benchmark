
def all_ints_div_by_both_two_nums(nums):
    result = []
    for i in range(20, 35):
        if (i % 36 == 0 and i % 89 == 0):
            result.append(i)
    return result
