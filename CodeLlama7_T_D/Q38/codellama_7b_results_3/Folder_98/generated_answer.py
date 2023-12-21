
def find_subset_of_length_n(set_elements):
    # Initialize a variable to store the number of subsets
    num_subsets = 0

    # Loop through all possible combinations of four elements
    for element1 in set_elements:
        for element2 in set_elements:
            for element3 in set_elements:
                for element4 in set_elements:
                    # If the current combination is not equal to the previous one, then it is a new subset
                    if element1 != element2 and element2 != element3 and element3 != element4:
                        num_subsets += 1

    return num_subsets
