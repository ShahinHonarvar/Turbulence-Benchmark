
def find_subset_of_length_n(set_of_elements):
    # Initialize a counter variable to keep track of the number of subsets
    count = 0

    # Iterate over all possible combinations of elements from the set
    for combination in itertools.combinations(set_of_elements, 77):
        # Increment the counter by 1 for each valid subset found
        count += 1

    # Return the final count of subsets of size 77
    return count
