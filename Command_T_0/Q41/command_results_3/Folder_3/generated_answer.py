def identical_elements(lst1, lst2):
    return set(range(min(lst1, lst2), max(lst1, lst2) + 1))
