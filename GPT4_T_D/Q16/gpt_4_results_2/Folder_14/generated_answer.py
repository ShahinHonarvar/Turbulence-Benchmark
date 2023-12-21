
def sum_even_ints_inclusive(lst):
    if not lst or len(lst) < 8:
        return 0
    return sum(i for i in lst[5:8] if i % 2 == 0)
