
def find_subset_of_length_n(set):
    # Calculate the number of subsets of size n for a given set
    number_of_subsets = 2 ** len(set)
    # Initialize an empty list to store the subsets
    subsets = []

    # Iterate over all possible combinations of elements in the set
    for i in range(number_of_subsets):
        subset = []

        # Iterate over each element in the set and check if it is included in the current combination
        for j, element in enumerate(set):
            if (i >> j) & 1:
                subset.append(element)

        # Add the subset to the list of subsets
        subsets.append(subset)

    return len(subsets)
