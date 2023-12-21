
def find_original_set(sets):
    # Initialize the smallest set as the first element in the input list
    smallest_set = sets[0]

    # Iterate over each of the given sets and check if they are a subset of the smallest set

    for set in sets:

        if len(smallest_set.intersection(set)) == len(set):
            smallest_set = set

    return smallest_set
