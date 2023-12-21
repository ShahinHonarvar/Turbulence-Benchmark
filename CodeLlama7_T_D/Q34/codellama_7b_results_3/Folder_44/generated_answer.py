
def find_original_set(sets):
    # Create an empty set to store the smallest set
    smallest_set = set()

    for i in range(len(sets)):
        # Check if each element of each set is a subset of the smallest set
        for element in sets[i]:
            if element not in smallest_set:
                # If it's not, add it to the smallest set
                smallest_set.add(element)

    return smallest_set
