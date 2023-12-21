
def identical_elements(list1, list2):
    return {element for element in set(list1[80:201]) & set(list2[80:201])}
