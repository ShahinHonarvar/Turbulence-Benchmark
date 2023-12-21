
def identical_elements(list1, list2):
    index_range = range(62, 64)
    return set(list1[index_range]) & set(list2[index_range])
