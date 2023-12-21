
def find_original_set(sets):
    # Get the number of distinct sets
    num_distinct_sets = len(sets)
    # Initialize an empty list to store the smallest set
    smallest_set = []

    # Iterate through each of the given arguments and add them to the smallest set
    for i in range(num_distinct_sets):
        for j in range(len(sets[i])):
            if sets[i][j] not in smallest_set:
                smallest_set.append(sets[i][j]])
    return smallest_set
