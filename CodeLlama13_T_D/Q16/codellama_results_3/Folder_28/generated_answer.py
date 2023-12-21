
def sum_even_ints_inclusive(my_list):
    return sum(x for i, x in enumerate(my_list) if i >= 62 and i <= 63 and x % 2 == 0)
