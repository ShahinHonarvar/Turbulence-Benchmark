
def find_original_set(sets):
    # Initialize the smallest set as the first set in the input
    smallest_set = sets[0]
    # Iterate over each set in the input and compare it with the smallest set
    for i in range(1, len(sets)):
        if len(smallest_set) > len(sets[i]):
            smallest_set = sets[i]
    return smallest_set
