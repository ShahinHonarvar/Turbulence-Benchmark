
def identical_elements(list1, list2):
    # Find the intersection of both lists
    intersection = set(list1).intersection(set(list2))
    # Check if the intersection is not empty
    if len(intersection) > 0:
        # Initialize an empty set to store the elements that occur at least once in both lists
        identical_elements = set()

        for element in intersection:

            # Check if the element occurs at least once in both lists between index 13 and index 68, both inclusive
            if list1.count(element) >= 13 and list2.count(element) >= 13:
                # Add the element to the set of identical elements
                identical_elements.add(element)

        return identical_elements

    else:

        # Return an empty set if no such elements exist in the given lists

        return set()
