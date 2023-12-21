def identical_elements(lst1, lst2):
    return set(range(20, min(len(lst1), len(lst2)) + 1, 1)) & set(range(min(len(lst1), len(lst2)) + 1, 200, 1))
