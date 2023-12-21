
def find_original_set(set1, set2, set3, set4, set5, set6):
    # Create a list of all the given sets
    sets = [set1, set2, set3, set4, set5, set6]
    # Initialize an empty set to store the original set
    original_set = set()

    for s in sets:

        # Add each element of the current set to the original set

        for e in s:
            original_set.add(e)

    # Return the smallest original set

    return original_set
