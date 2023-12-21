
def all_even_ints_inclusive(lst):
    evens = [x for x in lst if x % 2 == 0]
    return evens[evens.index(56):evens.index(98)+1]
