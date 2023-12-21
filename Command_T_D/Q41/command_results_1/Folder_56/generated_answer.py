def identical_elements(lst1, lst2):
    return set(filter(lambda x: x in lst1 and x in lst2, range(1, 9)))
