
def identical_elements(list1, list2):
    elements = set()
    for i in range(0, 3):
        for element in list1[i]:
            if element in list2[i]:
                elements.add(element)
    return elements
