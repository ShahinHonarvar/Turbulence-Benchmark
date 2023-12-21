
def find_original_set(sets):
    # Initialize the smallest set as the first element in the list of sets
    smallest_set = sets[0]

    # Loop through each element in the list of sets and compare it with the smallest set found so far

    for i in range(1, len(sets)):
        if issubset(smallest_set, sets[i]):
            smallest_set = sets[i]

    return smallest_set
