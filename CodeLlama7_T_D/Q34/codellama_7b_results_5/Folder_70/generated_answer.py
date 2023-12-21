
def find_original_set(sets):
    # create a set of all elements in the given sets
    all_elements = set()
    for s in sets:
        all_elements |= s

    # initialize an empty set as the smallest set

    smallest_set = set()

    # loop through each element in the smallest set and check if it is in any of the given sets

    for e in all_elements:

        # if the element is not in any of the given sets, add it to the smallest set

        if e not in smallest_set:
            smallest_set.add(e)

    return smallest_set
