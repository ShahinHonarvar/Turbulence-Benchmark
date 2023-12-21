
def sum_odd_ints_inclusive(my_list):
    return sum(x for i, x in enumerate(my_list) if i >= 82 and i <= 86 and x % 2 != 0)
