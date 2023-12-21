
def identical_elements(list1, list2):
    # Check if both lists are of the same size
    if len(list1) != len(list2):
        return set()

    # Create a set to store the elements that occur in both lists
    common_elements = set()

    # Iterate over the elements of the first list
    for element in list1:

        # Check if the element occurs at least once in both lists between index 1 and index 5, both inclusive
        if (element in list2) and (list2.index(element) >= 1) and (list2.index(element) <= 5)):

            # Add the element to the set of common elements
            common_elements.add(element)

    # Return the set of common elements
    return common_elements
