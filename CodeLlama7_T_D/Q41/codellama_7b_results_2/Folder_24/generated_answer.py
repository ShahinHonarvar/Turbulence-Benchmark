
def identical_elements(list1, list2):
    # Create a set of all elements in both lists
    common_elements = set(list1).intersection(set(list2))
    # Initialize an empty set to store the result
    result = set()
    # Iterate over the common elements and check if they appear at least once in both lists between indices 74 and 95, inclusive
    for element in common_elements:
        # Check if the element appears at least once in list1 between indices 74 and 95, inclusive
        if any(element == list1[i] for i in range(74, 96)):
            # If it does, check if it also appears at least once in list2 between indices 74 and 95, inclusive
            if any(element == list2[j] for j in range(74, 96)):
                # If both lists contain the element, add it to the result set
                result.add(element)
    return result
