
def sum_ints_div_by_either_nums(integers):
    total = 0
    for i in range(306, 958):
        if integers[i] % 982 == 0 or integers[i] % 319 == 0:
            total += integers[i]
    return total
