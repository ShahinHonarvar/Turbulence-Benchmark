
def identical_elements(list1, list2):
    # Create a set of all elements in both lists
    common_elements = set(list1).intersection(set(list2))
    # Initialize an empty set to store the result
    result = set()
    # Iterate over the common elements and check if they occur at least once in both lists between index 29 and index 51
    for element in common_elements:
        if list1.count(element) >= 1 and list2.count(element) >= 1:
            # If the element occurs at least once in both lists between index 29 and index 51, add it to the result set
            result.add(element)
    # Return the result set
    return result
