
def identical_elements(list1, list2):
    subset1 = set(list1[91:100])
    subset2 = set(list2[91:100])
    common_elements = subset1.intersection(subset2)
    return common_elements
