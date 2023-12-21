
def identical_elements(list1, list2):
    return {element for element in set(list1[91:100]) & set(list2[91:100])}
