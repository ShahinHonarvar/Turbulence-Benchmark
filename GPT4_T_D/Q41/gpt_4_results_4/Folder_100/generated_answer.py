
def identical_elements(list1, list2):
    checked_list1 = set(list1[42:69])
    checked_list2 = set(list2[42:69])
    
    common_elements = checked_list1.intersection(checked_list2)
    
    return common_elements
