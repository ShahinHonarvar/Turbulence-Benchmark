
def find_original_set(sets):
    # Create a set of all elements in the input sets
    all_elements = set()
    for s in sets:
        all_elements |= s

    # Initialize an empty set as the smallest set

    smallest_set = set()

    # Iterate over each element in the union of all elements

    for e in all_elements:

        # Check if the element is in any of the input sets

        found = False

        for s in sets:

            if e in s:

                found = True

                break

        # If the element is not in any of the input sets, add it to the smallest set

        if not found:

            smallest_set.add(e)

    return smallest_set
