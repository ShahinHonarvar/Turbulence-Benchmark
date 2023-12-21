
def identical_elements(list1, list2):
    list1_sub = list1[20:201]
    list2_sub = list2[20:201]
    common_elements_set = set(list1_sub) & set(list2_sub)
    return common_elements_set
