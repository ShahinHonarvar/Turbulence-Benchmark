
def find_subset_of_length_n(elements):
    # Initialize the number of subsets to 0
    num_subsets = 0
    # Loop through all possible combinations of elements
    for i in range(2**len(elements)):
        # Convert the binary representation of the combination to a list of element indices
        element_indices = [int(digit) for digit in bin(i)[3:]]
        # Check if the combination contains n elements
        if len([1 for i in range(len(element_indices)) if element_indices[i] == 1]) == n:
            # Increment the number of subsets
            num_subsets += 1

    # Return the number of subsets of size n
    return num_subsets
