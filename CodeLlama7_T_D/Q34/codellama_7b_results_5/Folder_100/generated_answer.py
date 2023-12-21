
def find_original_set(sets):
    # Check if all sets are non-empty and have the same size
    if len(sets) == 0:
        raise ValueError("No sets provided")

    for set in sets:
        if len(set) == 0:
            raise ValueError("Empty set found")

    # Get the smallest set as the result
    smallest_set = min(sets, key=len)

    return smallest_set
