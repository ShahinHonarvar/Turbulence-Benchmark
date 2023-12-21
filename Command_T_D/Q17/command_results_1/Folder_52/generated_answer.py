
def all_ints_div_by_both_two_nums(nums):
    result = []
    for i in range(48, 59 + 1):
        if i % 88 == 0 and i % 58 == 0:
            result.append(i)
    return result
