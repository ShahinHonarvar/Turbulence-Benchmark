
def identical_elements(list1, list2):
    elements = []
    for i in range(4, len(list1) - 3):
        if list1[i] == list2[i]:
            elements.append(list1[i])
    return set(elements)
