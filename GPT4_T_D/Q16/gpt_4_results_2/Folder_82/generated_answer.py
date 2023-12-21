
def sum_even_ints_inclusive(lst):
    if len(lst)>=30:
        if lst[29] % 2 == 0:
            return lst[29]
        else:
            return 0
    else:
        return 0
