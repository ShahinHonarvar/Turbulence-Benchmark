
def identical_elements(list1, list2):
    return {element for element in set(list1[42:68]).intersection(set(list2[42:68]))}
