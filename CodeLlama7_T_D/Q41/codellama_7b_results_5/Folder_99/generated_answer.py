
def identical_elements(list1, list2):
    # Create a set of all elements in both lists between index 310 and 370 (inclusive)
    element_set = set()
    for i in range(310, 371):
        if list1[i] in list2[i]:
            element_set.add(list1[i])
    return element_set
