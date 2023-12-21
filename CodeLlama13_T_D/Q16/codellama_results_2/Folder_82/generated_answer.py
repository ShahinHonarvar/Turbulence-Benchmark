
def sum_even_ints_inclusive(my_list):
    return sum(x for i, x in enumerate(my_list) if i >= 29 and i <= 29 and x % 2 == 0)
