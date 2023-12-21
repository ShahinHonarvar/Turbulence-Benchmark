
def identical_elements(list1, list2):
    list1_sub = list1[56:67]
    list2_sub = list2[56:67]
    common_elements = set(list1_sub).intersection(set(list2_sub))
    return common_elements
