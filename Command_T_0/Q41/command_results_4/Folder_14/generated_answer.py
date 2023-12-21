def identical_elements(lst1, lst2):
    return set(range(min(5, len(lst1), len(lst2)), max(5, len(lst1), len(lst2)) + 1))
