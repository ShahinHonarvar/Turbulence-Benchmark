def sum_even_ints_inclusive(lst):
    return sum(x for x in lst[62:-2] if x % 2 == 0)
