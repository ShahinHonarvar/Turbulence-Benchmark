
def sum_ints_div_by_either_nums(integers):
    sum = 0
    for i in range(90, 98):
        if integers[i] % 13 == 0 or integers[i] % 35 == 0:
            sum += integers[i]
    return sum
