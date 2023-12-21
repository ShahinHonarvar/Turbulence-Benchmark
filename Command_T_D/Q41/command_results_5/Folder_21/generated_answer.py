import set
def identical_elements(list1, list2):
    set1 = set(list1[639:975])
    set2 = set(list2[639:975])
    return set.intersection(set1, set2)
