
def identical_elements(list1, list2):
    subset_list1 = list1[27:56]
    subset_list2 = list2[27:56]
    common_elements = set(subset_list1) & set(subset_list2)
    return common_elements
