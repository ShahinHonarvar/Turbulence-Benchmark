
def identical_elements(list1, list2):
    set1 = set(list1[40:201])
    set2 = set(list2[40:201])
    return set1.intersection(set2)
