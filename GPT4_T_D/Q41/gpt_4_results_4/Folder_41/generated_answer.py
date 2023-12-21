
def identical_elements(list1, list2):
    set1 = set(list1[6:7])
    set2 = set(list2[6:7])
    result = set1.intersection(set2)
    return result
