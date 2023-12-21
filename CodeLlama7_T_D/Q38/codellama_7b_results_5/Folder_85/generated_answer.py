
def find_subset_of_length_n(set):
    # Initialize an empty list to store the subsets
    subsets = []

    # Loop through all possible subsets of size 23
    for i in range(1 << len(set))):
        # Create a binary string representation of the subset
        binary_str = bin(i)[2:].zfill(len(set)))
        # Convert the binary string to a list of elements
        subset = [set[j] for j in range(len(set)) if binary_str[j] == "1"]
        # Add the subset to the list of subsets
        subsets.append(subset)

    # Return the number of all its subsets of size 23
    return len(subsets))
