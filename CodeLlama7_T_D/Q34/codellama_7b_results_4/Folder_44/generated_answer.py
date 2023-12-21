
def find_original_set(sets):
    # Create a list of all elements in the given sets
    all_elements = []
    for set in sets:
        all_elements.extend(set)

    # Sort the list of all elements
    all_elements.sort()

    # Initialize the smallest set to the first element in the sorted list
    smallest_set = {all_elements[0]}

    # Iterate through each of the remaining elements in the sorted list
    for i in range(1, len(all_elements)):
        # If the current element is not already in the smallest set
        if all_elements[i] not in smallest_set:
            # Add it to the smallest set
            smallest_set.add(all_elements[i])

    return smallest_set
