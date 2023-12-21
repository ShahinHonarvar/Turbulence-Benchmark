
def find_original_set(sets):
    # Create a set to store all elements
    all_elements = set()

    # Iterate over each set and add its elements to the all_elements set
    for s in sets:
        all_elements |= s

    # Initialize an empty set to store the smallest set
    smallest_set = set()

    # Iterate over each element in the all_elements set and check if it is present in any of the given sets
    for e in all_elements:
        for s in sets:
            if e in s:
                smallest_set.add(e)
                break

    return smallest_set
