
def identical_elements(list1, list2):
    return {element for element in set(list1[60:201]) if element in set(list2[60:201])}
