
def find_original_set(sets):
    # Create a copy of the input sets for reference
    original_sets = sets.copy()
    # Initialize an empty set to store the smallest subset
    smallest_subset = set()

    # Loop through each element in the first set and check if it is present in all other sets
    for element in original_sets[0]:
        present_in_all = True

        # Check if the element is present in all other sets
        for i in range(1, len(original_sets)):
            if element not in original_sets[i]:
                present_in_all = False
                break

        # If the element is present in all other sets, add it to the smallest subset
        if present_in_all:
            smallest_subset.add(element)

    return smallest_subset
