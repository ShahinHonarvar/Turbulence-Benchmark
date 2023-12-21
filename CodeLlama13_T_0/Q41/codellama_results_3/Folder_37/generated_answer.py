
def identical_elements(list1, list2):
    return {element for element in list1[1:6] if element in list2[1:6]}
