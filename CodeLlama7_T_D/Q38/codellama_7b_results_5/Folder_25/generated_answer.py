
def find_subset_of_length_n(set_of_elements):
    # Initialize a variable to store the number of subsets
    number_of_subsets = 0
    # Iterate over all possible combinations of elements
    for combination in itertools.combinations(set_of_elements, 90):
        # Increment the number of subsets by 1 for each valid combination
        number_of_subsets += 1
    # Return the total number of subsets of size 90
    return number_of_subsets
