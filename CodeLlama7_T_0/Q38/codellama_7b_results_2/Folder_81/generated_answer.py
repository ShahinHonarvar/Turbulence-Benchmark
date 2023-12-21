
def find_subset_of_length_n(set):
    # Initialize a variable to store the number of subsets
    num_subsets = 0

    # Iterate over all possible combinations of elements in the set
    for i in range(len(set) + 1):
        for j in range(i + 1, len(set) + 1):
            # If the combination is of size 20, increment the number of subsets
            if j - i == 20:
                num_subsets += 1

    # Return the number of all its subsets of size 20
    return num_subsets
