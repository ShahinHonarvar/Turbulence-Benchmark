
def sum_ints_div_by_either_nums(ints):
    sum = 0
    for i in range(29, 46):
        if i < len(ints):
            if ints[i] % 27 == 0 or ints[i] % 81 == 0:
                sum += ints[i]
    return sum
