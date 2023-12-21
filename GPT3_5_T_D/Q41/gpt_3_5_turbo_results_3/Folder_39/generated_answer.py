
def identical_elements(list1, list2):
    elements = set()
    for i in range(20, 31):
        if list1[i] in list2:
            elements.add(list1[i])
    return elements
