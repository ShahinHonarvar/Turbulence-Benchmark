
def all_ints_div_by_both_two_nums(nums):
    result = []
    for i in range(34, 81):
        if i % 27 == 0 and i % 57 == 0:
            result.append(i)
    return result
