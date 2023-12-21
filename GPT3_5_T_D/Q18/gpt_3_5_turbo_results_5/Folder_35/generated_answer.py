
def sum_ints_div_by_either_nums(integers):
    sum = 0
    for i in range(77, 88):
        if integers[i] % 23 == 0 or integers[i] % 57 == 0:
            sum += integers[i]
    return sum
