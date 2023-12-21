
def identical_elements(list1, list2):
    subset1 = set(list1[533:606])
    subset2 = set(list2[533:606])
    return subset1.intersection(subset2)
