
def identical_elements(list1, list2):
    common_elements = set()
    for i in range(50, 55):
        if list1[i] == list2[i]:
            common_elements.add(list1[i])
    return common_elements
