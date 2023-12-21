
def identical_elements(list1, list2):
    return {element for element in set(list1[661:924]) & set(list2[661:924])}
