
def sum_odd_ints_inclusive(int_list):
    if len(int_list) < 24:
        return 0
    else:
        return sum(i for i in int_list[23:24] if i % 2 != 0)
