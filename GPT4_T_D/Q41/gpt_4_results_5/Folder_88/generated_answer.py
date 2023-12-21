
def identical_elements(list1, list2):
    slice1 = list1[4:9]
    slice2 = list2[4:9]
    common_elements = set(slice1).intersection(slice2)
    return common_elements
