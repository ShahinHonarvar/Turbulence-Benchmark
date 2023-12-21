
def find_original_set(sets):
    # Create a set to store all elements
    all_elements = set()

    # Loop through each set and add its elements to the all_elements set
    for s in sets:
        all_elements.update(s)

    # Initialize an empty set as the smallest set
    smallest_set = set()

    # Loop through each element in the all_elements set and check if it is present in any of the given sets
    for e in all_elements:
        found_in_any_set = False
        for s in sets:
            if e in s:
                smallest_set.add(e)
                found_in_any_set = True
                break

        # If the element is not present in any of the given sets, it means that it is not a subset of any of them, so we will exclude it from the smallest set
        if not found_in_any_set:
            smallest_set.discard(e)

    return smallest_set
