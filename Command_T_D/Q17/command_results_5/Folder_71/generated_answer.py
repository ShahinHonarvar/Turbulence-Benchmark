
def all_ints_div_by_both_two_nums(nums):
    result = []
    for i in range(68, 99):
        if i % -37 == 0 and i % -26 == 0:
            result.append(i)
    return result
