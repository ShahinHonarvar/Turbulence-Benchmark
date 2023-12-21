
def all_ints_div_by_both_two_nums(nums):
    result = []
    for i in range(315, 934):
        if i % -897 == i % -556 == 0:
            result.append(i)
    return result
