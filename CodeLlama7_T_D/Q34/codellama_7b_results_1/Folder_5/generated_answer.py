
def find_original_set(sets):
    # Create a list of all sets
    all_sets = []
    for set in sets:
        all_sets.extend(set)
    # Find the smallest set that contains all elements
    smallest_set = None
    for element in all_sets:
        if smallest_set is None or len(smallest_set) > 1:
            smallest_set = {element}


    return smallest_set
