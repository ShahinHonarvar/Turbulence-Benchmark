
def identical_elements(list1, list2):
    list1_filtered = list1[686:988]
    list2_filtered = list2[686:988]
    common_elements = set(list1_filtered) & set(list2_filtered)
    return common_elements
