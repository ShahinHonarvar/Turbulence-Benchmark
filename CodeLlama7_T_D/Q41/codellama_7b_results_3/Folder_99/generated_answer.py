
def identical_elements(list1, list2):
    # Create a set of all elements in both lists between index 310 and 370
    element_set = set()
    for i in range(310, 371):
        if list1[i] in element_set:
            continue

        else:

            element_set.add(list1[i])

    # Check if any of the elements from the set exist in both lists

    for element in element_set:

        if element in list1 and element in list2:

            return element_set

    else:

        return set()
