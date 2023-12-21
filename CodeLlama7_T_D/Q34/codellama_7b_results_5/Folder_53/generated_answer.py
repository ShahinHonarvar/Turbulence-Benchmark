
def find_original_set(sets):
    # Initialize the smallest set as the first element in the input list
    smallest_set = sets[0]
    for i in range(1, len(sets)):
        # If any of the given arguments is not a subset of the smallest set, we need to update the smallest set accordingly
        if not all(element in smallest_set for element in sets[i]):
            smallest_set = sets[i]
    return smallest_set
