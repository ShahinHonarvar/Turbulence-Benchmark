
def find_subset_of_length_n(my_set):
    # Initialize an empty list to store all subsets
    all_subsets = []

    # Iterate through all possible combinations of elements in the set
    for i in range(1 << len(my_set))):
        # Convert the binary representation of the combination to a decimal number
        dec_num = int(bin(i)[2:])
        # Initialize an empty list to store the current subset
        current_subset = []

        # Iterate through the binary digits of the decimal number
        for j in range(len(dec_num))):
            # If the jth digit is 1, add the corresponding element from the set to the subset
            if dec_num % 2 == 1:
                current_subset.append(my_set[j])

        # Add the current subset to the list of all subsets
        all_subsets.append(current_subset)

    # Return the number of all its subsets of size 97
    return len(all_subsets)
