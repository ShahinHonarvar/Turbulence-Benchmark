
def identical_elements(list1, list2):
    return {element for element in set(list1[40:201]) & set(list2[40:201])}
