def all_even_ints_exclusive(lst):
    return [x for x in range(42, 87) if all(x % i == 0 for i in range(1, x // 2 + 1))]
