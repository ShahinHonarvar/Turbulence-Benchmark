
def identical_elements(list1, list2):
    # Create a set of all elements in both lists
    common_elements = set(list1).intersection(set(list2))
    # Check if any common elements occur at least once in both lists
    # anywhere between index 0 and index 3, both inclusive
    for element in common_elements:
        if list1.count(element) > 0 and list2.count(element) > 0:
            if (list1.index(element)) <= 3 and (list2.index(element)) <= 3:
                return {element}

    # If no common elements occur at least once in both lists
    # anywhere between index 0 and index 3, both inclusive
    return set()
