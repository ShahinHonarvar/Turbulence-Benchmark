
def all_even_ints_inclusive(lst):
    return [x for x in lst if x % 2 == 0 and lst.index(x) <= 1]
