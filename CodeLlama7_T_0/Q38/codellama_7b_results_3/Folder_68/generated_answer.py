
def find_subset_of_length_n(set):
    # Initialize a variable to store the number of subsets
    num_subsets = 0

    # Iterate over all possible combinations of three elements in the set
    for element1 in set:
        for element2 in set:
            for element3 in set:
                # If the combination is valid (i.e., it does not contain duplicates)
                if element1 != element2 and element2 != element3 and element3 != element1:
                    # Increment the number of subsets
                    num_subsets += 1

    # Return the number of subsets of size 3 in the set
    return num_subsets
