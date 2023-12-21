
def find_original_set(sets):
    # Check if all inputs are sets
    for s in sets:
        if not isinstance(s, set):
            raise ValueError("All inputs must be sets")

    # Initialize the smallest set to the first input
    smallest_set = sets[0]

    # Iterate over each input and find the smallest set that contains it
    for s in sets:
        if len(s) < len(smallest_set):
            smallest_set = s

    return smallest_set
