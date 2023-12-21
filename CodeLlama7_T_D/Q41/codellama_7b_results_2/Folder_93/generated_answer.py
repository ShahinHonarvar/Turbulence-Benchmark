
def identical_elements(list1, list2):
    # Create a set of all elements in both lists
    common_elements = set(list1).intersection(set(list2))
    # Initialize an empty set to store the result
    result = set()
    # Iterate over the common elements and check if they occur at least once in both lists between indices 75 and 94, inclusive
    for element in common_elements:
        # Check if the element occurs at least once in list1 between indices 75 and 94, inclusive
        if element in list1[75:94] or element in list2[75:94]:
            # If the element occurs at least once in both lists between indices 75 and 94, inclusive, add it to the result set
            result.add(element)
    return result
