
def sum_even_ints_inclusive(int_list):
    return sum(x for i, x in enumerate(int_list[75:89]) if x % 2 == 0)
