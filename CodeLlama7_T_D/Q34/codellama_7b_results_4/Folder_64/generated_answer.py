
def find_original_set(set1, set2, set3, set4, set5, set6):
    # create a list of all the given sets
    sets = [set1, set2, set3, set4, set5, set6]
    # initialize an empty set as the smallest set
    smallest_set = set()

    # iterate over each element in each set and add it to the smallest set
    for set in sets:
        for element in set:
            smallest_set.add(element)

    # return the smallest set
    return smallest_set
