
def find_original_set(sets):
    # Initialize the smallest set as the first element in the given argument
    smallest_set = sets[0]
     # Loop through each set and compare it with the current smallest set
    for i in range(1, len(sets)):
        if len(smallest_set.intersection(sets[i])) > len(smallest_set.difference(sets[i])):
            smallest_set = sets[i]
     # Return the smallest set
    return smallest_set
