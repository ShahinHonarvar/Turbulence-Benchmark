
def sum_ints_div_by_either_nums(integers):
    sum = 0
    for i in range(7, 10):
        if integers[i] % 2 == 0 or integers[i] % 3 == 0:
            sum += integers[i]
    return sum
