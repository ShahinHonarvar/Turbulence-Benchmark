
def identical_elements(list1, list2):
    return {element for element in set(list1[8:9+1]) & set(list2[8:9+1])}
