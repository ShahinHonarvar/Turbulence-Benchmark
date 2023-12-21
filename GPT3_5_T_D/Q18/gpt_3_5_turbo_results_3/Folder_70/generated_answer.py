
def sum_ints_div_by_either_nums(integers):
    sum = 0
    for i in range(42, 44):
        if integers[i] % 15 == 0 or integers[i] % 87 == 0:
            sum += integers[i]
    return sum
