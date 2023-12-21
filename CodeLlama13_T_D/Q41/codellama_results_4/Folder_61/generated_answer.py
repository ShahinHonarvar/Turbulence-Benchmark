
def identical_elements(list1, list2):
    return {x for x in list1[0:7] if x in list2[0:7]}
