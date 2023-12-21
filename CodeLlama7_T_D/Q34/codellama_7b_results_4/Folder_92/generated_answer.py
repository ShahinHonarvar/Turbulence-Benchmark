
def find_original_set(set1, set2, set3, set4, set5, set6, set7):
    # Combine all sets into a single list
    all_sets = [set1, set2, set3, set4, set5, set6, set7]
    # Create an empty set to store the smallest set
    smallest_set = set()

    # Iterate through each element in the list of sets
    for element in all_sets:
        # Check if the current element is a subset of the smallest set
        if element <= smallest_set:
            # If it is, add it to the smallest set
            smallest_set |= element

    # Return the smallest set
    return smallest_set
