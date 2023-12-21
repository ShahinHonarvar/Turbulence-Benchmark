def sum_odd_ints_inclusive(lst):
    return sum(n for n in range(10, 66) if n % 2 == 1 and n in lst)
