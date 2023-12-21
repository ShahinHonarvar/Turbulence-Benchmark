
def find_original_set(set1, set2, set3, set4):
    # Create a new set that contains all the elements from the given sets
    combined_set = set1 | set2 | set3 | set4
    # Initialize an empty set to store the smallest subset
    smallest_subset = set()

    # Iterate through each element in the combined set and check if it is present in at least one of the given sets
    for element in combined_set:
        if (element in set1) or (element in set2) or (element in set3) or (element in set4):
            # If an element is present in at least one of the given sets, add it to the smallest subset
            smallest_subset.add(element)

    return smallest_subset
