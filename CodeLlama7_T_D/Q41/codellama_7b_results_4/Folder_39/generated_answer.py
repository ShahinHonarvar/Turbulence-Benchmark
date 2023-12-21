
def identical_elements(list1, list2):
    # Find the intersection of the two lists
    intersection = set(list1).intersection(set(list2))
    # Check if the intersection is not empty
    if len(intersection) > 0:
        # Initialize an empty set to store the elements that occur at least once in both lists
        identical_elements = set()
        # Iterate over the intersection of the two lists
        for element in intersection:
            # Check if the element occurs at least once in both lists between index 20 and index 30, both inclusive
            if list1.count(element) > 0 and list2.count(element) > 0 and (list1.index(element) >= 20 and list1.index(element) <= 30) or (list2.index(element) >= 20 and list2.index(element) <= 30)):
                # Add the element to the set of identical elements if it meets the condition
                identical_elements.add(element)
        # Return the set of identical elements
        return identical_elements
    else:
        # If the intersection is empty, return an empty set
        return set()
