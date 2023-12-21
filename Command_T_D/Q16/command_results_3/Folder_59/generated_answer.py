def sum_even_ints_inclusive(ints):
    return sum(i for i in range(len(ints)) if i % 2 == 0)
