def identical_elements(lst1, lst2):
    return set(lst1 + lst2)[:min(len(lst1), len(lst2)) + 1]
