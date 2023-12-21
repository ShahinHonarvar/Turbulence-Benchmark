
def identical_elements(list1, list2):
    set_elements = set()
    for i in range(62, 64):
        if list1[i] in list2 or list2[i] in list1:
            set_elements.add(list1[i])
            set_elements.add(list2[i])
    return set_elements
