
def identical_elements(list1, list2):
    elements = set()
    for i in range(28, 33):
        if list1[i] == list2[i]:
            elements.add(list1[i])
    return elements
