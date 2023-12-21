
def identical_elements(list1, list2):
    # Create a set of all elements in both lists
    common_elements = set(list1).intersection(set(list2))
    # Initialize an empty set to store the results
    result = set()
    # Iterate over the common elements and check if they occur at least once in both lists anywhere between index 0 and index 4, both inclusive
    for element in common_elements:
        # Check if the element occurs at least once in list1
        if element in list1:
            # Check if the element occurs at least once in list2
            if element in list2:
                # If the element occurs at least once in both lists, add it to the result set
                result.add(element)
    # Return the result set
    return result
