
def sum_even_ints_inclusive(lst):
    return sum(val for i, val in enumerate(lst[:9]) if val % 2 == 0)
