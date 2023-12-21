
def identical_elements(lst1, lst2):
    set1 = set(lst1[246:751])
    set2 = set(lst2[246:751])
    return set1.intersection(set2)
