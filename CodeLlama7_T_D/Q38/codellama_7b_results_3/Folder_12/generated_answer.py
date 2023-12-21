
def find_subset_of_length_n(set):
    # Initialize the number of subsets to 0
    num_subsets = 0
    # Loop through all possible combinations of 2 elements from the set
    for i in range(len(set)):
        for j in range(i+1, len(set)):
            # Increment the number of subsets by 1
            num_subsets += 1
    return num_subsets
