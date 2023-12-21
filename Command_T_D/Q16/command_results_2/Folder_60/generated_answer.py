def sum_even_ints_inclusive(lst):
    return sum(i for i in range(max(75, len(lst) - 1), min(85, len(lst))) if lst[i] % 2 == 0)
