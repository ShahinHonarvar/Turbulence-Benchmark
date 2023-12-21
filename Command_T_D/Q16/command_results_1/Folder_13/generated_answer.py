def sum_even_ints_inclusive(lst):
    even = [x for x in lst[25:87] if x % 2 == 0]
    return sum(even) if even else 0
