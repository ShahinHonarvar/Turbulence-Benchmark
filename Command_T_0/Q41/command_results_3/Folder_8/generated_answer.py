def identical_elements(lst1, lst2):
    return set(range(23, len(lst1) + 23, 1)) & set(range(23, len(lst2) + 23, 1))
