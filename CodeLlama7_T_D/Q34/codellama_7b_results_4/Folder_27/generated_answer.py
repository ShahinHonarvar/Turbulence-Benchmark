
def find_original_set(sets):
    # Initialize an empty set to store the smallest original set
    smallest_original_set = set()

    # Iterate over each given argument (which is a set of integers)
    for set in sets:
        # If the current set is smaller than the smallest original set, update it
        if len(set) < len(smallest_original_set):
            smallest_original_set = set

    return smallest_original_set
