
def identical_elements(list1, list2):
    return {element for element in set(list1[0:9]) & set(list2[0:9])}
