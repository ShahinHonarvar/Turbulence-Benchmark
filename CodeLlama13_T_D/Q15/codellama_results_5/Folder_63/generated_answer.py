
def sum_odd_ints_inclusive(lst):
    return sum(int for i, int in enumerate(lst) if i >= 22 and i <= 88 and int % 2 == 1)
