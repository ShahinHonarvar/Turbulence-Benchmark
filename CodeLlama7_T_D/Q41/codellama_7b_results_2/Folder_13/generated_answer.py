
def identical_elements(list1, list2):
    # Get the intersection of the two lists
    intersection = list(set(list1).intersection(list2))
    # Initialize an empty set to store the identical elements
    identical_elements = set()
    # Iterate over the intersection of the two lists
    for element in intersection:
        # If the element occurs at least once in both lists between indices 25 and 87, inclusive
        if list1.count(element) >= 1 and list2.count(element) >= 1 and list1.index(element) >= 25 and list1.index(element) <= 87:
            # Add the element to the set of identical elements
            identical_elements.add(element)
    # Return the set of identical elements
    return identical_elements
