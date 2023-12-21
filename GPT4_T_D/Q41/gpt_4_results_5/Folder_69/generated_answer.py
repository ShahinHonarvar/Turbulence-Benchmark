
def identical_elements(lst1, lst2):
    set1 = set(lst1[32:36])
    set2 = set(lst2[32:36])
    return set1.intersection(set2)
