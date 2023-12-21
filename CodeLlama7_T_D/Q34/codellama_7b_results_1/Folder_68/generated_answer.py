
def find_original_set(set1, set2, set3):
    smallest_set = None
    # Find the smallest set among the three given sets
    if len(set1) < len(set2) and len(set1) < len(set3):
        smallest_set = set1

    elif len(set2) < len(set1) and len(set2) < len(set3):
        smallest_set = set2

    else:

        smallest_set = set3

    # Return the smallest set that is a subset of all three given sets
    return smallest_set
