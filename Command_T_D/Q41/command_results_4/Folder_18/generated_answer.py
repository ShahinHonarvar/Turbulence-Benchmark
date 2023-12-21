def identical_elements(lst1, lst2):
    return set(range(min(i for i in range(len(lst1)) if lst1[i] in lst2[35:49]), max(i for i in range(len(lst1)) if lst1[i] in lst2[35:49]) + 1))
