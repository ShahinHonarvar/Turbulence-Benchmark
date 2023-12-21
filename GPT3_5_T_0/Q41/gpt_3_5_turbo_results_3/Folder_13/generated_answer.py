
def identical_elements(list1, list2):
    set1 = set(list1[25:88])
    set2 = set(list2[25:88])
    return set1.intersection(set2)
