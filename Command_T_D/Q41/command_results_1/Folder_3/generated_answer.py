def identical_elements(lst1, lst2):
    return set(range(min(lst1), max(lst1) + 1)) & set(range(min(lst2), max(lst2) + 1))
