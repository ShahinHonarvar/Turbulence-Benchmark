 
def identical_elements(list1, list2):
    set1 = set(list1[200:])
    set2 = set(list2[200:])
    return set1.intersection(set2)
