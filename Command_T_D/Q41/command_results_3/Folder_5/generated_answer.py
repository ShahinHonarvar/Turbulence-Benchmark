def identical_elements(lst1, lst2):
    return set(x for x in range(min(lst1), max(lst1) + 1) if x in lst1 and x in lst2)
