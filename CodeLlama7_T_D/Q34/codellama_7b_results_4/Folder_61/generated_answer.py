
def find_original_set(set1, set2, set3, set4):
    # Create a new set that contains all elements from the given sets
    original_set = set1 | set2 | set3 | set4
    # Return the smallest set that contains all elements from the given sets
    return min(original_set)
