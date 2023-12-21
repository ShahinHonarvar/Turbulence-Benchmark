
def sum_odd_ints_inclusive(my_list):
    return sum(x for i, x in enumerate(my_list) if i >= 91 and i <= 99 and x % 2 != 0) or 0
