def sum_odd_ints_inclusive(lst):
    return sum(i for i in range(len(lst)-1, -1, 2) if lst[i] % 2 == 1)
