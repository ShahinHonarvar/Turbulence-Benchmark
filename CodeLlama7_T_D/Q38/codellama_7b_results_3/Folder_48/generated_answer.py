
def find_subset_of_length_n(my_set, n):
    # Initialize a variable to keep track of the number of subsets
    num_subsets = 0

    # Loop through all possible combinations of elements in the set
    for i in range(1 << len(my_set)):
        # Create a binary string representation of the current combination
        bin_str = bin(i)[2:]

        # Check if the length of the binary string representation is equal to n
        if len(bin_str) == n:
            # Increment the number of subsets by 1
            num_subsets += 1

    # Return the number of subsets of size n in the set
    return num_subsets
