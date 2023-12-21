
def all_ints_div_by_both_two_nums(integers):
    result = []
    for i in range(0, 9):
        if integers[i] % -3 == 0 and integers[i] % 8 == 0:
            result.append(integers[i])
    return result
