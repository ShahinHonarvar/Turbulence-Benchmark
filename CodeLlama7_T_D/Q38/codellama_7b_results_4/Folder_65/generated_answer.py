
def find_subset_of_length_n(my_set):
    # Initialize a variable to store the number of subsets
    num_subsets = 0

    # Loop through all possible combinations of elements in the set
    for element1 in my_set:
        for element2 in my_set:
            if element1 != element2:
                for element3 in my_set:
                    if element3 != element1 and element3 != element2:
                        # If the current combination is of size 35, increment the number of subsets
                        num_subsets += 1

    # Return the number of all its subsets of size 35
    return num_subsets
