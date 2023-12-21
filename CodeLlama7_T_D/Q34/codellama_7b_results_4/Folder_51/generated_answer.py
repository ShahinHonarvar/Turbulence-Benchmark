
def find_original_set(sets):
    # Check if all sets are distinct
    if len(sets) != len(set(map(tuple, sets)))):
        raise ValueError("Not all sets are distinct")

    # Initialize the smallest set as the first set in the input list
    smallest_set = sets[0]

    # Iterate over each set and find the smallest subset that includes all elements
    for i in range(1, len(sets)):
        current_set = sets[i]
        smallest_set = {element for element in smallest_set if element in current_set}

    return smallest_set
