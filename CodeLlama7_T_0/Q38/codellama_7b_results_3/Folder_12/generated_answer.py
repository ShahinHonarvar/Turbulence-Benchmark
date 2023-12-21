
def find_subset_of_length_n(set):
    # Initialize a variable to store the number of subsets
    num_subsets = 0

    # Iterate over all possible combinations of two elements from the set
    for element1 in set:
        for element2 in set:
            # If both elements are different, increase the number of subsets by 1
            if element1 != element2:
                num_subsets += 1

    # Return the number of all its subsets of size 27
    return num_subsets
