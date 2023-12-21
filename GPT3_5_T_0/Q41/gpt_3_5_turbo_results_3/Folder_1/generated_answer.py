
def identical_elements(list1, list2):
    set1 = set(list1[31:73])
    set2 = set(list2[31:73])
    return set1.intersection(set2)
