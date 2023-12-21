
def find_original_set(sets):
    # Create a list of all elements in the sets
    elements = []
    for set in sets:
        elements += set

    # Remove duplicates from the list of elements

    unique_elements = list(set(elements))

    # Initialize the smallest set as the first set in the input list

    smallest_set = sets[0]

    # Iterate over each set in the input list and compare it to the smallest set found so far

    for set in sets:

        # If the current set is smaller than the smallest set, update the smallest set

        if len(set) < len(smallest_set):

            smallest_set = set


    return smallest_set
