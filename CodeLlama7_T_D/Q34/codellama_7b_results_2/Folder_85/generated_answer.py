
def find_original_set(sets):
    # initialize the smallest set as the first element in sets
    smallest_set = sets[0]

    # loop through each set and check if it is a subset of the smallest set
    for i in range(1, len(sets)):
        if is_subset(smallest_set, sets[i]):
            continue

        else:

            # update the smallest set with the current set
            smallest_set = sets[i]

    return smallest_set

def is_subset(set1, set2):
    # check if all elements in set1 are also present in set2
    for element in set1:
        if element not in set2:
            return False

    return True
