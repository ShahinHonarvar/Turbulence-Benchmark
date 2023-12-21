
def find_original_set(sets):
    # Initialize the smallest set as the first argument
    smallest_set = sets[0]
    # Iterate over each argument and compare it to the current smallest set
    for i in range(1, len(sets)):
        if len(sets[i]) < len(smallest_set):
            smallest_set = sets[i]
    return smallest_set
