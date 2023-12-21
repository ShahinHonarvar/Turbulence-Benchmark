def all_odd_ints_inclusive(lst):
    lst = [int(i) for i in lst]
    return [i for i in range(37, 77, 2) if i in lst]
