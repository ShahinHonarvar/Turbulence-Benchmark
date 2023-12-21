
def identical_elements(list1, list2):
    # Find the intersection of both lists
    intersection = set(list1).intersection(set(list2))
    # Check if the intersection is not empty
    if len(intersection) > 0:
        # Initialize an empty set to store the elements that occur at least once in both lists
        identical_elements = set()

        # Iterate over the intersection of both lists
        for element in intersection:
            # Check if the element occurs at least once in both lists between index 90 and index 200, both inclusive
            if list1.count(element) >= 1 and list2.count(element) >= 1 and (list1.index(element) >= 90 and list1.index(element) <= 200) or (list2.index(element) >= 90 and list2.index(element) <= 200)):
                # Add the element to the set of identical elements
                identical_elements.add(element)

        # Return the set of identical elements
        return identical_elements

    # If no such elements exist in the given lists, return an empty set
    else:
        return set()
