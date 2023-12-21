import itertools
def identical_elements(lst1, lst2):
    return set(x for x in itertools.zip_longest(lst1, lst2, fillvalue=None) if x[0] == x[1])
