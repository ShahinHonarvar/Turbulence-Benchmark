
def all_even_ints_inclusive(lst):
    return [x for x in range(min(lst), max(lst)+1, 2) if x in lst]
