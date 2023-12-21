
def sum_odd_ints_inclusive(integer_list):
    return sum(val for i, val in enumerate(integer_list[22:51]) if val % 2 != 0)
