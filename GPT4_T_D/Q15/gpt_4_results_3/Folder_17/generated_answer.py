
def sum_odd_ints_inclusive(lst):
    sublist = lst[62:79]
    return sum(i for i in sublist if i % 2 != 0)
