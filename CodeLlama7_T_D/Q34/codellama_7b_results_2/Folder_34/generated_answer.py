
def find_original_set(sets):
    # Initialize the smallest set with the first element
    smallest_set = {sets[0]}
    # Iterate over each element of the given sets
    for i in range(len(sets)):
        # Add each element to the smallest set if it is not already present
        for elem in sets[i]:
            if elem not in smallest_set:
                smallest_set.add(elem)
    return smallest_set
