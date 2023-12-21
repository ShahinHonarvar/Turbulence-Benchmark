
def identical_elements(list1, list2):
    set_elements = set()
    if len(list1) != len(list2):
        return set_elements
    for i in range(37, 52):
        if list1[i] in list2:
            set_elements.add(list1[i])
    return set_elements
