
def all_ints_div_by_both_two_nums(nums):
    result = []
    for i in range(55, 85):
        if i % -24 == 0 and i % -11 == 0:
            result.append(i)
    return result
