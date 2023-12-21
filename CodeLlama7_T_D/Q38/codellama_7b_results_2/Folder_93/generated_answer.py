
def find_subset_of_length_n(set):
    # Initialize a variable to keep track of the number of subsets
    num_subsets = 0

    # Loop through all possible combinations of elements in the set
    for i in range(len(set) + 1):
        for j in range(i + 1, len(set) + 1):
            for k in range(j + 1, len(set) + 1):
                # If the current combination is of size 45, increment the number of subsets
                if (k - i) == 45:
                    num_subsets += 1

    # Return the number of subsets of size 45
    return num_subsets
