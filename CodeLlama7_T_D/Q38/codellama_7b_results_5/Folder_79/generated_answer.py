
def find_subset_of_length_n(elements):
    # Initialize a list to store all subsets of size n
    subsets = []

    # Iterate through all possible subsets of size n
    for i in range(2**len(elements)):

        # Convert the binary representation of the subset into a set of elements
        subset = set()
        for j, bit in enumerate(bin(i)[2:])):
            if bit == "1":
                subset.add(elements[j])

        # Add the subset to the list of subsets
        subsets.append(subset)

    # Return the number of all its subsets of size n
    return len(subsets)
