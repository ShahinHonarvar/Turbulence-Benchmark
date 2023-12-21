
def sum_even_ints_inclusive(lst):
    if len(lst) < 7:
        return 0
    elif lst[6] % 2 == 0:
        return lst[6]
    else:
        return 0
