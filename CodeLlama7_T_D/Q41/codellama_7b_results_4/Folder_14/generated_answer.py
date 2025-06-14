
def identical_elements(list1, list2):
    # Create a set of all elements in both lists
    common_elements = set(list1).intersection(set(list2))
    # Return an empty set if there are no common elements

    if not common_elements:
        return set()

    # Iterate through the elements in both lists and check if they occur at least once in both lists between index 5 and index 7, inclusive
    for element in common_elements:
        count = 0
        for i in range(5, 8):
            if element in list1[i] or element in list2[i]:
                count += 1

        # If the element occurs at least once in both lists between index 5 and index 7, inclusive, add it to the final set of identical elements
        if count >= 2:
            identical_elements.add(element)

    return identical_elements
