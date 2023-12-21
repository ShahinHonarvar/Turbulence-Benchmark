def identical_elements(lst1, lst2):
    return set(range(min(9, len(lst1)), max(9, len(lst1)) + 1)) & set(range(min(9, len(lst2)), max(9, len(lst2)) + 1))
