
def sum_odd_ints_inclusive(lst):
    return sum(filter(lambda x: x % 2 != 0, lst[:6]))
