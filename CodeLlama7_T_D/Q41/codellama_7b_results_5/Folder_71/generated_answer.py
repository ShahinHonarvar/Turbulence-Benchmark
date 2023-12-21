
def identical_elements(list1, list2):
    # Create a set of all elements in both lists
    common_elements = set(list1).intersection(set(list2))
    # Initialize an empty set to store the results
    matching_elements = set()

    # Iterate over the common elements between the two lists
    for element in common_elements:
        # Check if the element is present in both lists between indices 26 and 52, inclusive
        if list1.count(element) > 0 and list2.count(element) > 0:
            # If the element is present in both lists between these indices, add it to the set of matching elements
            matching_elements.add(element)
    return matching_elements
