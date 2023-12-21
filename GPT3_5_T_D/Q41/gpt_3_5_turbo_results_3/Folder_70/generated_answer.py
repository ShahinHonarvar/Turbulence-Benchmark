
def identical_elements(list1, list2):
    set_list1 = set(list1[28:33])
    set_list2 = set(list2[28:33])
    return set_list1.intersection(set_list2)
