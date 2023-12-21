
def find_original_set(sets):
    # Create a set to store all the elements
    all_elements = set()

    # Loop through each set and add its elements to the all_elements set
    for s in sets:
        all_elements |= s

    # Return the smallest set that contains all the elements from the given sets
    return min(sets, key=len), all_elements
