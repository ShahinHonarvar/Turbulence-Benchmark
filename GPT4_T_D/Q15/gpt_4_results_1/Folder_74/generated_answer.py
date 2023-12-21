
def sum_odd_ints_inclusive(int_list):
    sum_odd = 0
    for i in range(17, 79):
        if (i < len(int_list)) and (int_list[i] % 2 != 0):
            sum_odd += int_list[i]
    return sum_odd
