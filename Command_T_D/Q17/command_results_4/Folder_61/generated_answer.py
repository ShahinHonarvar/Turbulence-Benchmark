
def all_ints_div_by_both_two_nums(nums):
    result = []
    for i in range(0, 6):
        if i % 5 == i % 6 == 0:
            result.append(i)
    return result
