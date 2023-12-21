
def find_original_set(sets):
    # Initialize the smallest set as the first element in the input list
    smallest_set = sets[0]
    for i in range(1, len(sets)):
        # Check if each element of the current set is also present in the smallest set
        for element in sets[i]:
            if element not in smallest_set:
                # If an element is not present in the smallest set, then the current set cannot be the smallest set
                break
        else:
            # If the loop completes without breaking, then all elements of the current set are also present in the smallest set
            smallest_set = sets[i]
    return smallest_set
