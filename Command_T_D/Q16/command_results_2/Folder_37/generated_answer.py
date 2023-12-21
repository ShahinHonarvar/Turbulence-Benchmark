def sum_even_ints_inclusive(ints):
    return sum(i for i in range(1, len(ints)+1) if i % 2 == 0)
