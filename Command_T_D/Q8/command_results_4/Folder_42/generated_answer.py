def all_even_ints_exclusive(lst):
    evens = [i for i in range(44, 67) if i % 2 == 0]
    return [e for e in lst[evens[0]:evens[-1]] if e % 2 == 0]
