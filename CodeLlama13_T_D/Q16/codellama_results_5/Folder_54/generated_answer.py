
def sum_even_ints_inclusive(my_list):
    return sum(x for i, x in enumerate(my_list) if i >= 34 and i <= 55 and x % 2 == 0)
