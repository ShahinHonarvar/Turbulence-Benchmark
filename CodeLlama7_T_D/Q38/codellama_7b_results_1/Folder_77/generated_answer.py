
def find_subset_of_length_n(my_set):
    # Initialize a variable to keep track of the number of subsets
    num_subsets = 0

    # Iterate over all possible combinations of three elements from the set
    for elem1 in my_set:
        for elem2 in my_set:
            for elem3 in my_set:
                if elem1 != elem2 and elem2 != elem3 and elem3 != elem1:
                    num_subsets += 1

    # Return the number of subsets of size three
    return num_subsets
