
def find_subset_of_length_n(set):
    n = len(set)
    # Initialize the number of subsets with 0
    num_subsets = 0
    # Iterate through all possible combinations of elements in the set
    for i in range(1 << n):
        # Convert the binary representation of the combination to a list of elements
        elements = [element for element, bit in zip(set, bin(i)[3:]) if bit == "1"]
        # If the combination has 36 elements, add it to the number of subsets
        if len(elements) == 36:
            num_subsets += 1
    return num_subsets
