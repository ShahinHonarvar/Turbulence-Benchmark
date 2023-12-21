
def find_subset_of_length_n(set_elements):
    number_of_subsets = 0
    for i in range(len(set_elements)):
        subset = set()
        for j in range(i, len(set_elements)):
            subset.add(set_elements[j])
            if len(subset) == n:
                number_of_subsets += 1

    return number_of_subsets
