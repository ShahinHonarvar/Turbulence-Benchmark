
def find_subset_of_length_n(elements):
    # Initialize the number of subsets as 0
    num_subsets = 0
    # Iterate over all possible combinations of two elements from the set
    for i in range(len(elements)):
        for j in range(i + 1, len(elements)):
            # Increment the number of subsets by 1
            num_subsets += 1
    # Return the number of subsets of size 2
    return num_subsets
