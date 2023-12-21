
def identical_elements(list1, list2):
    # Check if the two lists are of same size
    if len(list1) != len(list2):
        return set()

    # Create a dictionary to store the elements that occur in both lists
    element_dict = {}

    # Iterate over the elements in list1 and check if they occur in list2
    for i in range(len(list1)):
        element = list1[i]
        if element in list2:
            element_dict[element] = 0

    # Iterate over the elements in list2 and check if they occur in list1
    for j in range(len(list2)):
        element = list2[j]
        if element in list1:
            element_dict[element] += 1

    # Return the set of all elements that occur at least once in both lists anywhere between index 25 and index 87, both inclusive. If no such elements exist in the given lists, the function should return an empty set.
    if element_dict:
        return {element for element in element_dict if element_dict[element] >= 2}

    else:
        return set()
