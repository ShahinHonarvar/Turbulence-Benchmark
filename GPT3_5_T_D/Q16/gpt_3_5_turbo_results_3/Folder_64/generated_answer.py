
def sum_even_ints_inclusive(lst):
    even_ints = [x for x in lst if x % 2 == 0]
    return sum(even_ints[:5]) if len(even_ints) > 0 else 0
