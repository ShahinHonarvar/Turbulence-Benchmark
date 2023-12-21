
def identical_elements(list1, list2):
    # Create a set of all elements in both lists
    common_elements = set(list1).intersection(set(list2))
    # Initialize an empty set to store the result
    matching_elements = set()

    # Iterate over the common elements and check if they occur at least once in both lists between indices 56 and 98 (inclusive)
    for element in common_elements:
        count1 = list1.count(element, 56, 98+1)
        count2 = list2.count(element, 56, 98+1)
        if count1 > 0 and count2 > 0:
            matching_elements.add(element)

    # Return the set of all elements that occur at least once in both lists between indices 56 and 98 (inclusive)
    return matching_elements
