
def all_even_ints_inclusive(lst):
    return [val for idx, val in enumerate(lst[262:747]) if val % 2 == 0]
