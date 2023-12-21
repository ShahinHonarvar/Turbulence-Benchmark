
def identical_elements(list1, list2):
    set1 = set(list1[246:751])
    set2 = set(list2[246:751])
    return set1.intersection(set2)
