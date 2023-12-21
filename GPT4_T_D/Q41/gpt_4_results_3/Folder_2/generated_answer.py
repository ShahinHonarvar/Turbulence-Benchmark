
def identical_elements(list1, list2):
    subset1 = set(list1[15:40])
    subset2 = set(list2[15:40])
    common_elements = subset1.intersection(subset2)
    return common_elements
