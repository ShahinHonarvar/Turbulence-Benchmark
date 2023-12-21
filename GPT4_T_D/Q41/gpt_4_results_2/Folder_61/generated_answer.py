
def identical_elements(list1, list2):
    subset1 = set(list1[:7])
    subset2 = set(list2[:7])
    intersection = subset1.intersection(subset2)
    return intersection
