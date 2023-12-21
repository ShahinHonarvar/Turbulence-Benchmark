
def identical_elements(list1, list2):
    return {element for element in set(list1[19:93]) & set(list2[19:93])}
