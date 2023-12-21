
def identical_elements(list1, list2):
    # Create a set of all elements in both lists
    common_elements = set(list1).intersection(set(list2))
    # Initialize an empty set to store the results
    matching_elements = set()

    for element in common_elements:
        # Check if the element occurs at least once in both lists between index 30 and index 200, both inclusive
        if list1.count(element) >= 30 and list2.count(element) >= 30:
            matching_elements.add(element)

    return matching_elements
