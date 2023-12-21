
def find_original_set(set1, set2):
    # Create a new set that contains all elements from set1 and set2
    combined_set = set1 | set2
    # Initialize an empty set to store the original sets
    original_sets = set()

    # Loop through each element in the combined set
    for element in combined_set:

        # If the current element is not in set1, add it to the original sets
        if element not in set1:
            original_sets.add(element)

        # If the current element is not in set2, add it to the original sets
        elif element not in set2:
            original_sets.add(element)

    # Return the smallest set of the original sets
    return min(original_sets, key=len)
