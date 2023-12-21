
def all_even_ints_inclusive(lst):
    return [i for i in range(min(lst), max(lst)+1) if i % 2 == 0]
