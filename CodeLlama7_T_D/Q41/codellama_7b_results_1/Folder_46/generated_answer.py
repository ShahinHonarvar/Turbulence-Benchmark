
def identical_elements(list1, list2):
    # Create a set of all elements in both lists
    common_elements = set(list1).intersection(set(list2))
    # Check if any element occurs at least once in both lists anywhere between index 30 and index 87, both inclusive.
    for element in common_elements:
        if list1.count(element) >= 30 and list2.count(element) >= 30:
            return {element}

    # If no such elements exist in the given lists, the function should return an empty set.
    return set()
