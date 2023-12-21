
def identical_elements(list1, list2):
    return {x for x in set(list1[0:5]) & set(list2[0:5])}
