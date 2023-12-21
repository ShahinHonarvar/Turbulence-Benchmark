
def find_subset_of_length_n(elements):
    # Initialize a list to store all subsets of size 36
    subsets = []

    # Iterate over all possible combinations of elements
    for i in range(len(elements) + 1):
        for j in range(i + 1, len(elements) + 1):
            for k in range(j + 1, len(elements) + 1):
                # If the current combination is of size 36, add it to the list of subsets
                if (k - j) == 36:
                    subsets.append((i, j, k)))

    # Return the number of all its subsets of size 36
    return len(subsets))
