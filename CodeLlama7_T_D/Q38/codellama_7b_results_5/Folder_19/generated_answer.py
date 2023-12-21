
def find_subset_of_length_n(elements):
    # Initialize a list to store all subsets
    all_subsets = []
    # Iterate over all possible combinations of elements
    for i in range(2**len(elements)):
        # Convert the binary representation of the combination to a decimal number
        dec = int(bin(i)[2:])
        # Initialize an empty list to store the current subset
        subset = []
        # Iterate over the elements and add the corresponding bit to the subset
        for j, element in enumerate(elements):
            if dec & (1 << j):
                subset.append(element)

        # Add the current subset to the list of all subsets
        all_subsets.append(subset)
    # Return the number of all subsets of size 13
    return len([subset for subset in all_subsets if len(subset) == 13])
