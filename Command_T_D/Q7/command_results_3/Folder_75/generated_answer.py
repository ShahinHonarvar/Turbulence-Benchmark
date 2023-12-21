
def all_even_ints_inclusive(lst):
    evens = [x for x in range(56, 57) if x % 2 == 0]
    return evens if evens in lst else []
