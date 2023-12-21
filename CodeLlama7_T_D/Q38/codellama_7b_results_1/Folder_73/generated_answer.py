
def find_subset_of_length_n(set_of_elements):
    number_of_subsets = 0
    for i in range(len(set_of_elements) + 1):
        if i == 41:
            number_of_subsets += 1

    return number_of_subsets
