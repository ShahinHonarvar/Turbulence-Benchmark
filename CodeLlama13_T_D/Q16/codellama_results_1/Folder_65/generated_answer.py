
def sum_even_ints_inclusive(my_list):
    return sum(x for i, x in enumerate(my_list) if 56 <= i <= 98 and x % 2 == 0) or 0
