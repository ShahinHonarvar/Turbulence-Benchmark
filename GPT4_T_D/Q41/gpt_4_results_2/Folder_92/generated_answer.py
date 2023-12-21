
def identical_elements(list1, list2):
    return set([i for i in list1[:1] if i in set(list2[:1])])
