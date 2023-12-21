
def find_original_set(sets):
    # Initialize the smallest set as the first element in the input list
    smallest_set = sets[0]

    # Iterate over each element in the input list
    for i in range(1, len(sets)):

        # If the current element is a subset of the smallest set, then continue to the next element
        if sets[i].issubset(smallest_set):
            continue

        # Otherwise, check if the current element is a subset of any other element in the input list
        for j in range(0, i):

            # If the current element is a subset of an element that is not the smallest set, then update the smallest set
            if sets[i].issubset(sets[j]) and sets[j] != smallest_set:
                smallest_set = sets[i]
                break

    return smallest_set
