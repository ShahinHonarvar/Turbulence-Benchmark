
def identical_elements(list1, list2):
    return {x for i in range(3) for x in (list1[i], list2[i])}
