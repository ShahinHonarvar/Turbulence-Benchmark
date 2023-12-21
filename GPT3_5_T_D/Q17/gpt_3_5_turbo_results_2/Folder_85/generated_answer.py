
def all_ints_div_by_both_two_nums(integers):
    result = []
    for i in range(1, 9):
        if integers[i] % -9 == 0 and integers[i] % -3 == 0:
            result.append(integers[i])
    return result
