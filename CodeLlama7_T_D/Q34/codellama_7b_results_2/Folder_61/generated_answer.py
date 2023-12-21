
def find_original_set(sets):
    # Initialize the smallest set with the first element of each set
    smallest_set = {*sets[0]}
    # Loop through each set and update the smallest set if necessary
    for i in range(1, len(sets)):
        if len(smallest_set) > len(sets[i]):
            smallest_set = sets[i]
    return smallest_set
