
def find_subset_of_length_n(set):
    # Initialize a list to store all subsets of size 21
    subsets = []

    # Iterate over all possible combinations of elements in the set
    for i in range(len(set) + 1):
        for j in range(i + 1, len(set) + 1):
            # Add the current combination to the list of subsets
            subsets.append((set[i], set[j])))

    # Return the number of all its subsets of size 21
    return len(subsets))
