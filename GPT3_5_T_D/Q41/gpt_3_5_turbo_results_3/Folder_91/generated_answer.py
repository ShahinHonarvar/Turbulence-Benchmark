
def identical_elements(list1, list2):
    set1 = set(list1[:5])
    set2 = set(list2[:5])
    return set1.intersection(set2)
