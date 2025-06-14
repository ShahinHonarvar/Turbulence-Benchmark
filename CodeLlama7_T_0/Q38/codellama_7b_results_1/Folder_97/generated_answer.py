
def find_subset_of_length_n(set):
    # Initialize a variable to store the number of subsets
    num_subsets = 0

    # Iterate over all possible combinations of elements in the set
    for i in range(len(set)):
        for j in range(i + 1, len(set)):
            # If the current combination is a subset of size n, increment the number of subsets
            if len({*set[i], *set[j]}) == n:
                num_subsets += 1

    # Return the number of all its subsets of size n
    return num_subsets
