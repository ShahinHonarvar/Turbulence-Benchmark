
def identical_elements(list1, list2):
    # Find the intersection of the two lists
    intersection = set(list1).intersection(set(list2))
    # Check if the intersection is not empty
    if len(intersection) > 0:
        # Initialize an empty set to store the identical elements
        identical_elements = set()
        # Iterate over the intersection of the two lists
        for element in intersection:
            # Check if the element occurs at least once in both lists between indices 52 and 71, both inclusive
            if list1.count(element) >= 1 and list2.count(element) >= 1 and (list1.index(element) >= 52 and list1.index(element) <= 71) or (list2.index(element) >= 52 and list2.index(element) <= 71)):
                # If the element occurs at least once in both lists between indices 52 and 71, both inclusive, add it to the set of identical elements
                identical_elements.add(element)
        return identical_elements
    else:
        # If no such elements exist in the given lists, return an empty set
        return set()
