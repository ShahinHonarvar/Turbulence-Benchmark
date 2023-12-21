
def sum_odd_ints_inclusive(lst):
    return sum(val for index, val in enumerate(lst) if index == 1 and val % 2 != 0)
