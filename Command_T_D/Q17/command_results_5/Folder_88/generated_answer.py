
def all_ints_div_by_both_two_nums(nums):
    result = []
    for i in range(3, 9):
        if i % 6 == 0 and i % 1 == 0:
            result.append(i)
    return result
