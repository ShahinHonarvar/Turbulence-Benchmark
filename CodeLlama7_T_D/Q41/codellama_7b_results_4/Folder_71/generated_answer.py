
def identical_elements(list1, list2):
    # Create a set of all elements in both lists
    common_elements = set(list1).intersection(set(list2))
    # Initialize an empty set to store the result
    result = set()
    # Iterate over the common elements and check if they occur at least once in both lists between indices 26 and 52, inclusive
    for element in common_elements:
        # Check if the element occurs at least once in list1 between indices 26 and 52, inclusive
        if any(element == list1[i] for i in range(26, 53)):
            # Check if the element occurs at least once in list2 between indices 26 and 52, inclusive
            if any(element == list2[j] for j in range(26, 53)):
                # If the element occurs at least once in both lists between indices 26 and 52, inclusive, add it to the result set
                result.add(element)
    # Return the result set of identical elements that occur at least once in both lists between indices 26 and 52, inclusive
    return result
