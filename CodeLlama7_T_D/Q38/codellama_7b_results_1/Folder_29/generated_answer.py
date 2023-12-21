
def find_subset_of_length_n(elements):
    n = len(elements)
    # Initialize a 2D array to store the subsets
    subsets = [[], []]

    for i in range(1, n + 1):
        # Add the current subset to the list of subsets
        subsets.append([])

        for j in range(0, n - i + 1):
            # Add the current element to the subset
            subsets[i].append(elements[j])

    return len(subsets)
