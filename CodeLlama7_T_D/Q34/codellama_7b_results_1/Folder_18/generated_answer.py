
def find_original_set(sets):
    # Initialize the smallest set as the first element of the input list
    smallest_set = sets[0]

    # Iterate through each set in the input list and compare it to the smallest set
    for i in range(1, len(sets)):
        if len(sets[i]) < len(smallest_set):
            smallest_set = sets[i]

    return smallest_set
