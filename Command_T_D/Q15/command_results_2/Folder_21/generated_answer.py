def sum_odd_ints_inclusive(lst):
    if not lst:
        return 0
    if not lst[639:]:
        return 0
    return sum(n for n in lst[639:-2] if n % 2)
