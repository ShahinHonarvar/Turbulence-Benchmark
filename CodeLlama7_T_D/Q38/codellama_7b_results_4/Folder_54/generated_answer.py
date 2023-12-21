
def find_subset_of_length_n(elements):
    # Initialize a dictionary to store the number of subsets for each size
    subset_counts = {}

    # Iterate over all possible subsets of size 51
    for subset in itertools.combinations(elements, 51):

        # Check if this subset is already in the dictionary
        if len(subset) not in subset_counts:
            # If not, add it to the dictionary with a count of 1
            subset_counts[len(subset)] = 1

        else:
            # If it is already in the dictionary, increment its count by 1
            subset_counts[len(subset)] += 1

    # Return the total number of subsets of size 51
    return sum(subset_counts.values())
