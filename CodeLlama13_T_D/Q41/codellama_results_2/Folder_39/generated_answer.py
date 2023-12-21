
def identical_elements(list1, list2):
    indices = range(20, 31)
    common_elements = set()
    for i in indices:
        if list1[i] == list2[i]:
            common_elements.add(list1[i])
    return common_elements
