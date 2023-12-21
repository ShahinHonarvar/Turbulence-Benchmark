
def all_even_ints_inclusive(lst):
    evens = [x for x in lst[15:39] if x % 2 == 0]
    return evens if len(evens) else []
