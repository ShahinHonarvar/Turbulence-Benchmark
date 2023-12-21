
def find_subset_of_length_n(elements):
    # Initialize a dictionary to store the number of subsets for each size
    subset_counts = {}

    # Iterate over all possible combinations of elements
    for combination in itertools.combinations(elements, 60):
        # Get the size of the current combination
        combination_size = len(combination)

        # Increment the count of subsets for the current size
        if combination_size in subset_counts:
            subset_counts[combination_size] += 1
        else:
            subset_counts[combination_size] = 1

    # Return the total number of subsets
    return sum(subset_counts.values())
