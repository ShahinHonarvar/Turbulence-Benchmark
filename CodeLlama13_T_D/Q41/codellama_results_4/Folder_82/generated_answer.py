
def identical_elements(list1, list2):
    return {x for x in set(list1[20:201]) & set(list2[20:201])}
