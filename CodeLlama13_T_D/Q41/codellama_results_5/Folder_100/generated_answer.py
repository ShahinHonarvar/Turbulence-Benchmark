
def identical_elements(list1, list2):
    indices = range(42, 69)
    elements = set()
    for i in indices:
        if list1[i] == list2[i]:
            elements.add(list1[i])
    return elements
