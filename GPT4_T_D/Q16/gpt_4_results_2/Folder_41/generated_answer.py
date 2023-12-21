
def sum_even_ints_inclusive(int_list):
    if 6 <= len(int_list) - 1:
        if int_list[6] % 2 == 0:
            return int_list[6]
        else:
            return 0
    else:
        return 0
