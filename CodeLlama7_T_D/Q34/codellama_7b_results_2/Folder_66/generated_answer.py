
def find_original_set(sets):
    # Initialize the smallest set as the first element in the input list
    smallest_set = sets[0]

    # Iterate over each set in the input list and compare it to the smallest set found so far

    for set in sets:

        if len(set) < len(smallest_set):
            smallest_set = set

    return smallest_set
