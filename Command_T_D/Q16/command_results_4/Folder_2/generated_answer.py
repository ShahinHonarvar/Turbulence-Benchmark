def sum_even_ints_inclusive(lst):
    return sum(i for i in range(15, 40) if i % 2 == 0 and i in lst)
