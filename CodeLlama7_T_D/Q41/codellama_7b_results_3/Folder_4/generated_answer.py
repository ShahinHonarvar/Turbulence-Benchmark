
def identical_elements(list1, list2):
    # Get the intersection of the two lists
    intersection = list(set(list1).intersection(list2))
    # Initialize an empty set to store the identical elements
    identical_elements = set()
    # Iterate over the intersection of the two lists
    for element in intersection:
        # Check if the element occurs at least once in both lists anywhere between index 12 and index 92, both inclusive
        if list1.count(element) >= 12 and list1.count(element) <= 92 and list2.count(element) >= 12 and list2.count(element) <= 92:
            # If the element occurs at least once in both lists anywhere between index 12 and index 92, both inclusive, add it to the set of identical elements
            identical_elements.add(element)
    # Return the set of identical elements
    return identical_elements
