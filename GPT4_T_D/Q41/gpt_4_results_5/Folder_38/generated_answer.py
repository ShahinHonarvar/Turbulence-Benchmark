
def identical_elements(list1, list2):
    subset1 = set(list1[22:64])
    subset2 = set(list2[22:64])
    common_elements = subset1.intersection(subset2)
    return common_elements
