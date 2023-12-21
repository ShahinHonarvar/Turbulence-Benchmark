
def identical_elements(list1, list2):
    elements = set()
    for i in range(4, len(list1)):
        if list1[i] in list2:
            elements.add(list1[i])
    return elements
