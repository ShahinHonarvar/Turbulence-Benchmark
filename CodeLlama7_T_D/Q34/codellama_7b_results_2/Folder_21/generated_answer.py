
def find_original_set(sets):
    # Initialize the smallest set with the first element
    smallest_set = {sets[0].pop()}
    # Iterate through each set and update the smallest set if necessary
    for set in sets:
        updated_smallest_set = False
        for element in smallest_set:
            if element not in set:
                break
        else:
            smallest_set.update(set)
            updated_smallest_set = True
        if not updated_smallest_set:
            return None

    # Return the smallest set
    return smallest_set
