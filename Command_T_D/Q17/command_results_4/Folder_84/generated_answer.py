
def all_ints_div_by_both_two_nums(nums):
    result = []
    for i in range(78, 81):
        if i % 76 == 0 and i % 60 == 0:
            result.append(i)
    return result
