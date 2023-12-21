
def identical_elements(list1, list2):
    # Create a set of all elements in both lists
    common_elements = set(list1).intersection(set(list2))
    # Check if there are any elements that occur at least once in both lists anywhere between index 30 and index 48, both inclusive.
    for element in common_elements:
        # Check if the current element occurs at least once in list1 between indices 30 and 48, inclusive.
        if any(element == item for item in list1[30:49]):
            # Check if the current element also occurs at least once in list2 between indices 30 and 48, inclusive.
            if any(element == item for item in list2[30:49]):
                # If the current element occurs at least once in both lists between indices 30 and 48, inclusive, add it to the set of identical elements.
                identical_elements.add(element)
    # Return the set of identical elements found.
    return identical_elements
