
def find_original_set(sets):
    # Create a set to store all elements from the input sets
    all_elements = set()

    for s in sets:
        # Add all elements from the current set to the set of all elements
        all_elements.update(s)

    # Initialize an empty set to store the smallest subset that contains all elements from the input sets
    smallest_subset = set()

    while all_elements:
        # Pop an element from the set of all elements
        element = all_elements.pop()

        # Add the element to the current subset
        smallest_subset.add(element)

        # Remove any elements that are not in the current subset from the set of all elements
        all_elements = all_elements - smallest_subset

    return smallest_subset
