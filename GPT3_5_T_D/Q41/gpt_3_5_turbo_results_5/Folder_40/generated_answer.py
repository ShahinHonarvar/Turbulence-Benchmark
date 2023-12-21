
def identical_elements(list1, list2):
    return set(list1[:list1.index(1)+1]) & set(list2[:list2.index(1)+1])
