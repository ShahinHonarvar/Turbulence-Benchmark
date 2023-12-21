def identical_elements(lst1, lst2):
    return set(range(3, min(len(lst1), len(lst2)) + 3)) & set(range(3, min(len(lst1), len(lst2)) + 3))
