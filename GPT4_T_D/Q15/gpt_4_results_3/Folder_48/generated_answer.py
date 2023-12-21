
def sum_odd_ints_inclusive(int_list):
    return sum(val for i, val in enumerate(int_list[533:606]) if val % 2 != 0)
