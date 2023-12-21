
def identical_elements(list1, list2):
    indices = range(28, 33)
    return {element for element in set(list1[indices]) & set(list2[indices])}
