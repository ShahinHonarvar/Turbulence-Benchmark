import itertools
def identical_elements(lst1, lst2):
    return set(x for x in itertools.intersection(lst1[52:71], lst2[52:71]))
