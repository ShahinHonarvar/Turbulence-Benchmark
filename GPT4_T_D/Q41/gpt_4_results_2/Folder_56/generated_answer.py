
def identical_elements(list1, list2):
    common_elements = set(list1[1:9]).intersection(set(list2[1:9]))
    return common_elements
