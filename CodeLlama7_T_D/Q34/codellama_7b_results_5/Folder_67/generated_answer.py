
def find_original_set(sets):
    # Get the smallest set from the input sets
    smallest_set = min(sets, key=len)
    # Check if the smallest set is already a subset of all the other sets
    if all(smallest_set.issubset(other_set) for other_set in sets):
        return smallest_set

    # Find the first set that is not a subset of the smallest set
    first_non_subset = next(set for set in sets if not smallest_set.issuperset(set)), None
    # If no such set exists, return the smallest set
    if first_non_subset is None:
        return smallest_set

    # Get the subset of the first non-subset set that is also a subset of the smallest set
    common_subset = smallest_set.intersection(first_non_subset)
    # If no such subset exists, return the smallest set
    if not common_subset:
        return smallest_set

    # Recursively call find_original_set with the common subset and the remaining sets as input
    return find_original_set(common_subset, *sets.difference({smallest_set}))
