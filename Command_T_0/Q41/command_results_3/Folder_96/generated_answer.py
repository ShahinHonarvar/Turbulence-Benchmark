def identical_elements(lst1, lst2):
    return set(range(50, 201)) & set(lst1[50:200]) & set(lst2[50:200])
