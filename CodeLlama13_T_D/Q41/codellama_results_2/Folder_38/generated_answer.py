
def identical_elements(list1, list2):
    return {x for x in set(list1[22:64]) & set(list2[22:64])}
