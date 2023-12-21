def find_subset_of_length_n(set_of_elements):
    n = 94
    count = 1
    for element in set_of_elements:
        count *= n - len(set_of_elements) + 1
    return count
