def sum_odd_ints_inclusive(lst):
    return sum(i for i in range(len(lst)-1, len(lst)-1, 2) if lst[i])
