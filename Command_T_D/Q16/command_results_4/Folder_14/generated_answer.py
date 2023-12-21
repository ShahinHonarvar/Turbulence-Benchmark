def sum_even_ints_inclusive(lst):
    return sum(n for n in lst[5:-2] if n % 2 == 0)
