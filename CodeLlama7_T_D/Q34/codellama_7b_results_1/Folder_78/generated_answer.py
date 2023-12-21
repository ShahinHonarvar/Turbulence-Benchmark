
def find_original_set(sets):
    # Check if all sets have the same size
    if len(set(map(len, sets))) != 1:
        raise ValueError("All sets must have the same size")

    # Get the smallest set and its size
    smallest_set = min(sets, key=len)
    smallest_set_size = len(smallest_set)

    # Initialize the result set with the smallest set
    result_set = {x for x in smallest_set}

    # Add elements from other sets to the result set if they are not already present
    for i in range(len(sets)):
        if i != len(sets) - 1:
            for element in sets[i + 1]:
                if element not in result_set:
                    result_set.add(element)

    # Return the smallest set found
    return result_set
