
def find_subset_of_length_n(set):
    # Initialize the result variable
    result = 0

    # Iterate over all possible subsets of length n
    for i in range(1 << len(set))):
        # Check if the current subset has size 630
        if sum(bin(i)[2:].zfill(len(set))) == 630:
            # Increment the result variable
            result += 1

    # Return the result variable
    return result
