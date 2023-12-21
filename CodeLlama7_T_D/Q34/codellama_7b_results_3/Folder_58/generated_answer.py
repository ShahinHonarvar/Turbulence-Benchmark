
def find_original_set(sets):
    # Create a set to store the original sets
    original_sets = set()

    # Loop through each of the given arguments and add them to the original sets
    for arg in sets:
        original_sets.add(arg)

    # Initialize an empty set to store the smallest set
    smallest_set = set()

    # Loop through each of the elements in each of the original sets
    for element in original_sets.pop():

        # Check if the current element is already in the smallest set
        if element in smallest_set:
            continue

        # Add the current element to the smallest set and break out of the loop
        smallest_set.add(element)
        break

    # Return the smallest set
    return smallest_set
