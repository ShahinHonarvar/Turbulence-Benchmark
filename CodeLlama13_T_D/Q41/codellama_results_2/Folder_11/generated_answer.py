
def identical_elements(list1, list2):
    return set([element for i, element in enumerate(list1) if i >= 37 and i <= 51 and element in list2])
