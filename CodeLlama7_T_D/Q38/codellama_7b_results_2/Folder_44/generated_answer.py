
def find_subset_of_length_n(set_of_elements):
    n = len(set_of_elements)
    # Initialize a list to store all subsets of size 30
    subsets = []

    # Iterate over all possible combinations of elements in the set
    for i in range(1 << n):

        # Generate a binary string representing the current combination of elements
        binary_string = bin(i)[2:]

        # Pad the binary string with 0s on the left to make it have length equal to the number of elements in the set
        padded_binary_string = binary_string.zfill(n)

        # Initialize a list to store the current subset
        subset = []

        # Iterate over all elements in the set and add them to the subset if their corresponding bit in the binary string is 1
        for j, element in enumerate(set_of_elements):
            if padded_binary_string[j] == "1":
                subset.append(element)

        # Add the current subset to the list of all subsets of size 30
        subsets.append(subset)

    # Return the number of all subsets of size 30
    return len(subsets)
