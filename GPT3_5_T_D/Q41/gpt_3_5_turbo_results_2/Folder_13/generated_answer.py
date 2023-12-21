
def identical_elements(lst1, lst2):
    set1 = set(lst1[25:88])
    set2 = set(lst2[25:88])
    return set1.intersection(set2)
