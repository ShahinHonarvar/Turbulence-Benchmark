
def identical_elements(list1, list2):
    list1_section = list1[75:89]
    list2_section = list2[75:89]
    return set(list1_section) & set(list2_section)
