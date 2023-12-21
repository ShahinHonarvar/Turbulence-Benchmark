
def all_ints_div_by_both_two_nums(nums):
    result = []
    for i in range(8, 10):
        if (i % 3 == 0 and i % 6 == 0) or (i % 3 == 1 and i % 6 == 2) or (i % 3 == 2 and i % 6 == 1):
            result.append(i)
    return result
