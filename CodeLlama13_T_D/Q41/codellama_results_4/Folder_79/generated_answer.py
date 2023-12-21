
def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    return {x for x in set(list1[4:8]) & set(list2[4:8])}
