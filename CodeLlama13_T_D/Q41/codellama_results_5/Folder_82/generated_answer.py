
def identical_elements(list1, list2):
    indices = range(20, 201)
    return set(element for element in list1 if element in list2 and any(element == list2[i] for i in indices))
