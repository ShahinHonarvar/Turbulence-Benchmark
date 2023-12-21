
def sum_odd_ints_inclusive(lst):
    return sum(n for i, n in enumerate(lst[60:201]) if n % 2 != 0)
