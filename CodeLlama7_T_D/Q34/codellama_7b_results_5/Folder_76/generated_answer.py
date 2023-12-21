
def find_original_set(sets):
    # Initialize the smallest set as the first element in the input list
    smallest_set = sets[0]

    # Iterate over the remaining elements in the input list
    for i in range(1, len(sets)):
        # If the current element is a subset of the smallest set, do nothing
        if sets[i].issubset(smallest_set):
            continue

        # Otherwise, check if the current element is a subset of any other set in the input list
        for j in range(0, i):
            # If the current element is a subset of another set in the input list, update the smallest set accordingly
            if sets[i].issubset(sets[j]):
                smallest_set = sets[j]
                break

    return smallest_set
