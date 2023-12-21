
def identical_elements(list1, list2):
    sub_list1 = list1[82:87]
    sub_list2 = list2[82:87]
    common_elements = set(sub_list1) & set(sub_list2)
    return common_elements
