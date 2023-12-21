
def identical_elements(list1, list2):
    return {x for x in set(list1[262:746]) & set(list2[262:746])}
