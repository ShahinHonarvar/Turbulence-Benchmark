
def find_original_set(sets):
    # Create a copy of the input sets list
    sets_copy = sets[:]
    # Initialize the smallest set as the first element in the input sets list
    smallest_set = sets[0]

    # Loop through each set in the input sets list and compare it to the current smallest set
    for set in sets_copy:
        if len(set) < len(smallest_set):
            smallest_set = set

    return smallest_set
