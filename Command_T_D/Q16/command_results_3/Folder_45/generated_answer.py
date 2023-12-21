def sum_even_ints_inclusive(lst):
    return sum(i for i in range(30, min(len(lst) - 1, 200), 2) if lst[i] % 2 == 0)
