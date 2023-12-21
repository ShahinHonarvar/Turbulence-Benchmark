
def sum_odd_ints_inclusive(my_list):
    return sum(x for i, x in enumerate(my_list) if i >= 1 and x % 2 != 0)
