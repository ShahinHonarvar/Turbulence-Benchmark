def identical_elements(lst1, lst2):
    return set(x for x in range(min(len(lst1), len(lst2)), max(len(lst1), len(lst2)) + 1) if lst1[x] in lst2 and lst2[x] in lst1)
