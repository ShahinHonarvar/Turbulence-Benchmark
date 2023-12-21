
def identical_elements(list1, list2):
    common_set = set(list1[0:3]).intersection(set(list2[0:3]))
    return common_set
