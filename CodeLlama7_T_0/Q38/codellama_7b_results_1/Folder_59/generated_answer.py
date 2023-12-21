
def find_subset_of_length_n(set):
    # Initialize a counter for the number of subsets
    count = 0

    # Iterate over all possible combinations of two elements in the set
    for element1 in set:
        for element2 in set:
            # If both elements are different, increase the counter by one
            if element1 != element2:
                count += 1

    # Return the number of subsets of size 2
    return count
