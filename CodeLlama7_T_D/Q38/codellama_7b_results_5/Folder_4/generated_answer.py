
def find_subset_of_length_n(set):
    n = len(set)
    # Initialization of the number of subsets
    num_subsets = 0

    # Iterating over all possible combinations of elements
    for i in range(1 << n):

        # Converting the binary representation of the combination to a set of elements
        subset = set()
        for j in range(n):
            if (i >> j) & 1:
                subset.add(set[j])

        # Checking if the subset has size 15
        if len(subset) == 15:

            # Incrementing the number of subsets
            num_subsets += 1

    return num_subsets
