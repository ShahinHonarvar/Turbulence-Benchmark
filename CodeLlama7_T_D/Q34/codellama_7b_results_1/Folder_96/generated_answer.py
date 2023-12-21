
def find_original_set(sets):
    # Create a list of all elements in the sets
    all_elements = []
    for set in sets:
        all_elements += list(set)
    # Remove duplicates from the list of all elements
    unique_elements = list(set(all_elements))
    # Initialize an empty set to store the smallest set
    smallest_set = set()

    # Add each element from the unique_elements list to the smallest_set until it is not possible to add any more elements without violating the subset relationship
    for element in unique_elements:
        smallest_set.add(element)

    # Return the smallest_set as the original set
    return smallest_set
