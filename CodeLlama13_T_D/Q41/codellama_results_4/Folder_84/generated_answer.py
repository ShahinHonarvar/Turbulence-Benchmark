
def identical_elements(list1, list2):
    element_set = set()
    for i in range(43, 87):
        if list1[i] == list2[i]:
            element_set.add(list1[i])
    return element_set
