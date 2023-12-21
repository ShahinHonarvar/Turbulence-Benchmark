
def sum_odd_ints_inclusive(my_list):
    return sum(x for i, x in enumerate(my_list) if i >= 54 and i <= 98 and x % 2 == 1)
