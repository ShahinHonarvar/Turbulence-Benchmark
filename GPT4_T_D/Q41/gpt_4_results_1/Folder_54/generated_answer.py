
def identical_elements(lst1, lst2):
    subset1 = set(lst1[34:56])
    subset2 = set(lst2[34:56])
    intersection = subset1 & subset2
    return intersection
