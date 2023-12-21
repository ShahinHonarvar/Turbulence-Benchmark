
def identical_elements(list1, list2):
    return {element for element in list1[200:200+1] if element in list2[200:200+1]}
