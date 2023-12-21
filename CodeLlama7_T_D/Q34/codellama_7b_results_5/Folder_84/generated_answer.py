
def find_original_set(sets):
    # Initialize an empty set to store the smallest set
    smallest_set = set()

    for arg in sets:
        # Add each element in the argument to the smallest set
        for element in arg:
            smallest_set.add(element)

    return smallest_set
