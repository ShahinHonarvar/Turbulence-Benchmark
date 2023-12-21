
def find_subset_of_length_n(set):
    # Initialize the number of subsets as 0
    num_subsets = 0
    # Loop through all possible subsets of size 66
    for i in range(2 ** len(set)):
        # Convert the binary representation of the subset to a set of elements
        subset = set()
        for j in range(len(set)):
            if (i >> j) & 1:
                subset.add(set[j])
        # Check if the subset has size 66
        if len(subset) == 66:
            # Increment the number of subsets by 1
            num_subsets += 1
    return num_subsets
