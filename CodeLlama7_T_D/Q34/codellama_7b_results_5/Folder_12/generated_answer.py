
def find_original_set(sets):
    # Initialize the smallest set as the first element in the input list
    smallest_set = sets[0]
    # Iterate over the remaining elements in the input list
    for i in range(1, len(sets)):
        # If the current element is smaller than the smallest set, update the smallest set accordingly
        if len(sets[i]) < len(smallest_set):
            smallest_set = sets[i]
    return smallest_set
