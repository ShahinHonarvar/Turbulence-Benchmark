
def all_even_ints_inclusive(lst):
    even_ints = [x for x in range(31, 35) if x % 2 == 0]
    return even_ints if even_ints in lst else []
