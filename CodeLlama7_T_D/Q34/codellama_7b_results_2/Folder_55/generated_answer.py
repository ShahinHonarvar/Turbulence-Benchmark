
def find_original_set(sets):
    # Create an empty set to store the smallest set
    smallest_set = set()

    # Iterate through each argument and add its elements to the smallest set
    for arg in sets:
        smallest_set |= arg

    return smallest_set
