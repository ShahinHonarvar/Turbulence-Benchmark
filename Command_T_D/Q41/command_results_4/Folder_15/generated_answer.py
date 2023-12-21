import set
def identical_elements(lst1, lst2):
    return set.intersection(lst1[2:-2], lst2[2:-2])
