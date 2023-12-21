
def sum_odd_ints_inclusive(lst):
    return sum(x for i, x in enumerate(lst[74:96]) if i % 2 == 1)
