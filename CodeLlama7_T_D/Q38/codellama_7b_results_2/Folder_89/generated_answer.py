
def find_subset_of_length_n(my_set):
    # Initialize a list to store all subsets
    all_subsets = []

    # Iterate over all possible combinations of elements in the set
    for i in range(2 ** len(my_set))):
        # Convert the binary number to a list of 0s and 1s
        binary_list = [int(i) for i in bin(i)[3:]]
        # Create a subset by selecting elements from the set based on the binary number
        subset = [my_set[j] for j in range(len(my_set)) if binary_list[j] == 1]
        # Add the subset to the list of all subsets
        all_subsets.append(subset)

    # Return the number of all subsets of size 18
    return sum(1 for s in all_subsets if len(s) == 18))
