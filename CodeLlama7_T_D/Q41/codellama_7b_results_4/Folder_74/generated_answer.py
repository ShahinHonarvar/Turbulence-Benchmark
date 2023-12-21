
def identical_elements(list1, list2):
    # Check if the lists are of the same size and return an empty set if not
    if len(list1) != len(list2):
        return set()
    # Create a set of all elements in both lists
    elements = set(list1).intersection(set(list2))
    # Check if any elements occur at least once in both lists between index 17 and index 78, inclusive
    for element in elements:
        count = 0

        for i in range(max(17, list1.index(element)), min(78, list2.index(element)))):
            if list1[i] == element or list2[i] == element:
                count += 1

        # If any elements occur at least once in both lists between index 17 and index 78, inclusive, add them to the set of identical elements
        if count > 0:
            return elements

    # Otherwise, return an empty set

    return set()
