
def sum_odd_ints_inclusive(lst):
    return sum(item for index, item in enumerate(lst[75:86]) if item % 2 != 0)
