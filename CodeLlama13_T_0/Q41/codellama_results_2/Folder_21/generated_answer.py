
def identical_elements(list1, list2):
    return {element for element in set(list1[639:975]) & set(list2[639:975])}
