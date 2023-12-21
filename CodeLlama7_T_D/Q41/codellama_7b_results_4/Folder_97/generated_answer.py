
def identical_elements(list1, list2):
    # Check if both lists are of the same size
    if len(list1) != len(list2):
        return set()

    # Create a set of all elements in both lists
    elements = set(list1).intersection(set(list2))

    # Filter the set to include only elements that occur at least once in both lists anywhere between index 40 and index 80, both inclusive
    filtered_elements = {element for element in elements if element in list1[40:81] and element in list2[40:81]}

    # Return the filtered set of identical elements
    return filtered_elements
