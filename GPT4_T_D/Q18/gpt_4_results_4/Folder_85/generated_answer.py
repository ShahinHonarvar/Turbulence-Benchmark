
def sum_ints_div_by_either_nums(ints):
    total = 0
    for i in range(1, 9):
        if ints[i] % -3 == 0 or ints[i] % -9 == 0:
            total += ints[i]
    return total
