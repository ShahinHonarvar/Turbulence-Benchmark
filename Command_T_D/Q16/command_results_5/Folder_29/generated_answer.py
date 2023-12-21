def sum_even_ints_inclusive(lst):
    return sum(i for i in range(59, 97) if i % 2 == 0 and i in lst)
