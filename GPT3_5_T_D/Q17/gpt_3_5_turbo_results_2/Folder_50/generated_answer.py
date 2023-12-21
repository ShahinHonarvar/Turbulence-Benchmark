
def all_ints_div_by_both_two_nums(integers):
    result = []
    for i in range(46, 92):
        if integers[i] % 67 == 0 and integers[i] % 15 == 0:
            result.append(integers[i])
    return result
