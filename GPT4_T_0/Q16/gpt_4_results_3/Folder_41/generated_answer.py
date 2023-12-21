
def sum_even_ints_inclusive(lst):
    if len(lst) < 7:
        return 0
    else:
        return lst[6] if lst[6] % 2 == 0 else 0
