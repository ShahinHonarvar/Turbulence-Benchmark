
def identical_elements(list1, list2):
    set1, set2 = set(list1[310:371]), set(list2[310:371])
    return set1.intersection(set2)
