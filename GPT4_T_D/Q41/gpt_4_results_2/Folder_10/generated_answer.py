
def identical_elements(list1, list2):
    range_list1 = list1[25:60]
    range_list2 = list2[25:60]
    common_elements = set(range_list1) & set(range_list2)
    return common_elements
