
def identical_elements(list1, list2):
    list1_subset = list1[262:747]
    list2_subset = list2[262:747]

    common_elements = set(list1_subset) & set(list2_subset)
    return common_elements
