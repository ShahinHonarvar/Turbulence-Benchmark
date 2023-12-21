
def sum_odd_ints_inclusive(lst):
    if not lst or len(lst) < 606:
        return 0
    else:
        return sum(i for i in lst[533:606] if i%2 != 0)
