
def find_original_set(set1, set2, set3, set4):
    # Create a list of all the given sets
    sets = [set1, set2, set3, set4]
    # Initialize an empty set to store the smallest set
    smallest_set = set()

    for i in range(len(sets)):
        # Iterate over each element in the current set and add it to the smallest set
        for element in sets[i]:
            smallest_set.add(element)

    return smallest_set
