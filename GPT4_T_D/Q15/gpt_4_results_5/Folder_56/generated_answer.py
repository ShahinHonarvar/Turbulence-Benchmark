
def sum_odd_ints_inclusive(int_list):
    if len(int_list) > 0 and int_list[0] % 2 != 0:
        return int_list[0]
    else:
        return 0
