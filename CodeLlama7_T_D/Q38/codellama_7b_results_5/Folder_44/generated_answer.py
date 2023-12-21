
def find_subset_of_length_n(my_set):
    # Initialize a list to store all subsets of size 30
    subsets = []

    # Iterate over all possible combinations of 30 elements from the input set
    for i in range(1 << len(my_set))
        # Create a subset of size 30 by selecting 30 elements from the input set
        subset = [my_set[j] for j in range(len(my_set)) if (1 << j) & i]

        # Add the subset to the list of all subsets of size 30
        subsets.append(subset)

    # Return the number of all subsets of size 30
    return len(subsets)
