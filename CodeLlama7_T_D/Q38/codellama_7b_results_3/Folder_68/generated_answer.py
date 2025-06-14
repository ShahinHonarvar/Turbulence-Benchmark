
def find_subset_of_length_n(set):
    # Initialize a variable to store the number of subsets
    num_subsets = 0

    # Loop through all possible combinations of three elements in the set
    for i in range(len(set)):
        for j in range(i+1, len(set)):
            for k in range(j+1, len(set)):
                # If a subset is found, increment the number of subsets
                num_subsets += 1

    return num_subsets
