
def identical_elements(list1, list2):
    set_62_63_1 = set(list1[62:64])
    set_62_63_2 = set(list2[62:64])
    return set_62_63_1.intersection(set_62_63_2)
