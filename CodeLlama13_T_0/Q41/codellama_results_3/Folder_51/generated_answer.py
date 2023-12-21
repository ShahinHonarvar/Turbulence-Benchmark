
def identical_elements(list1, list2):
    return {element for element in list1[0:3] if element in list2[0:3]}
