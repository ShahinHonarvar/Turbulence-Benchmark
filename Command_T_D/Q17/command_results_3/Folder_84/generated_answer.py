
def all_ints_div_by_both_two_nums(lst):
    result = []
    for x in range(78, 81):
        if 76 % x == 0 and 60 % x == 0:
            result.append(x)
    return result
