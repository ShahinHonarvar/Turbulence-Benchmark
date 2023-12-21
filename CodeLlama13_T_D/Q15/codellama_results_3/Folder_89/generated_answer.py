
def sum_odd_ints_inclusive(lst):
    odds = [x for x in lst[56:83] if x % 2 == 1]
    return sum(odds) or 0
