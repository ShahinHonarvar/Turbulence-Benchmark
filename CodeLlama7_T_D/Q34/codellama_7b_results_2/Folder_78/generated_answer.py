
def find_original_set(sets):
    # Initialize the smallest set as the first element in the input list
    smallest_set = sets[0]
    # Loop through each of the given arguments
    for i in range(1, len(sets)):
        # If the current argument is a subset of the smallest set, do nothing
        if all(element in smallest_set for element in sets[i]):
            continue

        # Otherwise, loop through each element in the current argument
        for element in sets[i]:
            # If the element is not already in the smallest set, add it
            if element not in smallest_set:
                smallest_set.add(element)

    return smallest_set
