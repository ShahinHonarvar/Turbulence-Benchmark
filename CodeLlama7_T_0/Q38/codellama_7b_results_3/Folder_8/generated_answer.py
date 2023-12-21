
def find_subset_of_length_n(set):
    # Initialize a counter for the number of subsets
    count = 0

    # Iterate over all possible combinations of elements in the set
    for i in range(len(set) + 1):
        for j in range(i + 1, len(set) + 1):
            for k in range(j + 1, len(set) + 1):
                # If the current combination is of size 49, increment the counter
                if (k - j) == 49:
                    count += 1

    # Return the number of subsets of size 49
    return count
