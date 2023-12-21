
def all_ints_div_by_both_two_nums(nums):
    result = []
    for i in range(56, 88 + 1):
        if i % -59 == 0 and i % -79 == 0:
            result.append(i)
    return result
