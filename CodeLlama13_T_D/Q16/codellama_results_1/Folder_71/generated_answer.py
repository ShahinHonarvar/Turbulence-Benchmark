
def sum_even_ints_inclusive(my_list):
    return sum(x for i, x in enumerate(my_list) if i >= 26 and i <= 52 and x % 2 == 0) or 0
