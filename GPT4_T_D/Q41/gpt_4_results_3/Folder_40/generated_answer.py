
def identical_elements(list1, list2):
    common_elements = set(list1[0:2]) & set(list2[0:2])
    return common_elements
