
def find_original_set(sets):
    # Initialize the smallest set as the first set in the list
    smallest_set = sets[0]
    # Iterate over the remaining sets and compare them with the smallest set
    for i in range(1, len(sets)):
        if is_subset(smallest_set, sets[i]):
            smallest_set = sets[i]
    return smallest_set

def is_subset(set1, set2):
    # Check if all elements of set2 are also in set1
    for element in set2:
        if element not in set1:
            return False

    # If all elements of set2 were also in set1, then set2 is a subset of set1
    return True
