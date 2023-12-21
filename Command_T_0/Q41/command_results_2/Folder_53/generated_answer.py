def identical_elements(lst1, lst2):
    return set(range(200, len(lst1) + 200, 1)) & set(range(200, len(lst2) + 200, 1))
