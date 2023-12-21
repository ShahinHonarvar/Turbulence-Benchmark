def sum_odd_ints_inclusive(lst):
    return sum(i for i in range(59, 97) if i % 2 == 1 and i in lst)
