def identical_elements(lst1, lst2):
    return set(range(len(lst1) - 1, -1, -1)) & set(range(len(lst2) - 1, -1, -1))
