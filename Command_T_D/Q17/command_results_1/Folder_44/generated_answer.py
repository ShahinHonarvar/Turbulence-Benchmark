
def all_ints_div_by_both_two_nums(nums):
    result = []
    for i in range(25, 71):
        if i % 74 == 0 and i % 15 == 0:
            result.append(i)
    return result
