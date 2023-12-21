
def sum_odd_ints_inclusive(int_list):
    sum_odd = 0
    if len(int_list) < 67:
        return 0
    else:
        for i in range(64, 67):
            if int_list[i] % 2 != 0:
                sum_odd += int_list[i]
    return sum_odd
