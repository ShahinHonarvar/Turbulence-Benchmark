
def identical_elements(list1, list2):
    elements = []
    for i in range(28, 39):
        if list1[i] == list2[i]:
            elements.append(list1[i])
    return set(elements)
