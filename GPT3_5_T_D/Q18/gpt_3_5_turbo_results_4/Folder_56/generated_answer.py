
def sum_ints_div_by_either_nums(integers):
    total = 0
    for i in range(7, 10):
        if integers[i] % -9 == 0 or integers[i] % -7 == 0:
            total += integers[i]
    return total
