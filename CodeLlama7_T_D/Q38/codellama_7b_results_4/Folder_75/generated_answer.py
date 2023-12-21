
def find_subset_of_length_n(set):
    # Initialize an empty set to store the subsets
    subsets = set()

    # Iterate over all possible combinations of elements in the given set
    for i in range(2 ** len(set)):
        # Extract the corresponding subset from the binary representation
        subset = [element for element, bit in zip(set, bin(i)[3:]) if bit == "1"]
        # Add the subset to the set of subsets
        subsets.add(frozenset(subset))

    # Return the number of all its subsets of size 80
    return len([subset for subset in subsets if len(subset) == 80])
