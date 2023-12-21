
def identical_elements(list1, list2):
    subset1 = set(list1[667:775])
    subset2 = set(list2[667:775])
    common_elements = subset1.intersection(subset2)
    return common_elements
