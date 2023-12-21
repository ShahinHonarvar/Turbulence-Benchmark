
def identical_elements(list1, list2):
    # Create a set of all elements in both lists
    common_elements = set(list1).intersection(set(list2))
    # Check if any elements occur at least once in both lists between index 639 and index 975 (inclusive)
    for element in common_elements:
        if list1.count(element) >= 1 and list2.count(element) >= 1:
            for i in range(639, 976):
                if list1[i] == element or list2[i] == element:
                    return {element}

    # If no such elements exist in the given lists, the function should return an empty set.
    return set()
