
def find_subset_of_length_n(set_of_elements):
    number_of_subsets = 0
    for i in range(1 << len(set_of_elements)):
        subset = set()
        for j in range(len(set_of_elements)):
            if i & (1 << j):
                subset.add(set_of_elements[j])
        if len(subset) == 45:
            number_of_subsets += 1
    return number_of_subsets
