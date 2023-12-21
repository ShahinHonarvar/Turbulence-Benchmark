
def find_original_set(sets):
    # Initialize the smallest set as the first set in the list
    smallest_set = sets[0]
    # Iterate over each set in the list
    for set in sets:
        # Check if the current set is a subset of the smallest set
        if all(elem in smallest_set for elem in set):
            # If it is, do nothing
            pass
        
        else:
            # Otherwise, make the current set the new smallest set
            smallest_set = set
    
    return smallest_set
