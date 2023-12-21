
def identical_elements(list1, list2):
    return {element for element in set(list1[17:79]) & set(list2[17:79])}
