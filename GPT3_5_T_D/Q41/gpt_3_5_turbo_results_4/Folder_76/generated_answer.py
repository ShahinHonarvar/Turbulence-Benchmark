
def identical_elements(list1, list2):
    elements = set()
    for i in range(686, 988):
        if i < len(list1) and i < len(list2):
            if list1[i] == list2[i]:
                elements.add(list1[i])
    return elements
