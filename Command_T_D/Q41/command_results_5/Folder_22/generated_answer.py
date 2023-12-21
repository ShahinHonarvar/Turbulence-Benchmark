def identical_elements(lst1, lst2):
    return set(range(40, 200)) & set(lst1[40:200]) & set(lst2[40:200])
