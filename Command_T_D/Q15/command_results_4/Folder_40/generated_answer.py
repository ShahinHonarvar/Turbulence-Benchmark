def sum_odd_ints_inclusive(lst):
    return sum(n for n in lst[0::2] if n % 2)
