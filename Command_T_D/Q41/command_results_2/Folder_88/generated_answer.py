import itertools
def identical_elements(lst1, lst2):
    return set(itertools.chain(lst1[4:8], lst2[4:8]))
