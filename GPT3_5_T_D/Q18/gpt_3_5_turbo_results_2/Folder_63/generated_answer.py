
def sum_ints_div_by_either_nums(integers):
    num_sum = 0
    for i in range(31, 51):
        if integers[i] % 81 == 0 or integers[i] % 64 == 0:
            num_sum += integers[i]
    return num_sum
