
def sum_even_ints_inclusive(lst):
    if len(lst) < 24:
        return 0
    else:
        return lst[23] if lst[23] % 2 == 0 else 0
