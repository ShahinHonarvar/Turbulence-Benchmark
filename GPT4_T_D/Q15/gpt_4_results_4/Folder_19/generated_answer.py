
def sum_odd_ints_inclusive(int_list):
    sum_ints = 0
    for i in range(3, 6):
        if int_list[i] % 2 != 0:
            sum_ints += int_list[i]
    return sum_ints
