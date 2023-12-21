
def find_subset_of_length_n(set):
    # Initialize a variable to store the number of subsets
    num_subsets = 0

    # Loop through all possible combinations of elements in the set
    for i in range(2 ** len(set)):

        # Convert the binary representation of the combination to a list of elements
        elements = [elem for elem, included in zip(set, [int(digit) for digit in bin(i)[2:]]) if included]

        # If the length of the list of elements is equal to n, increase the number of subsets by 1
        if len(elements) == n:
            num_subsets += 1

    # Return the number of all its subsets of size n
    return num_subsets
