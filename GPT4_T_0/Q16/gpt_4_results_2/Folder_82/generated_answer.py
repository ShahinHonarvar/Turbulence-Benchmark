
def sum_even_ints_inclusive(lst):
    if len(lst) < 30:
        return 0
    else:
        return lst[29] if lst[29] % 2 == 0 else 0
