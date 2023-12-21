
def find_original_set(set1, set2):
    # Check if both sets are non-empty and have at least one element in common
    if not set1 or not set2 or len(set1.intersection(set2)) == 0:
        return None

    # Find the smallest set that contains all elements from both given sets
    original_set = set()

    for element in set1:
        if element in set2:
            original_set.add(element)

    return original_set
