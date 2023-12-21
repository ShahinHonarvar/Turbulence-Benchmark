
def sum_even_ints_inclusive(integer_list):
    return sum(x for i, x in enumerate(integer_list[25:60]) if x % 2 == 0)
