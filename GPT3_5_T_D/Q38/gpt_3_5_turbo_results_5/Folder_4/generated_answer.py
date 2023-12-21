
def find_subset_of_length_n(elements):
    if len(elements) < 15:
        return 0
    else:
        num_subsets = 1
        for i in range(15):
            num_subsets *= len(elements) - i
            num_subsets //= i + 1
        return num_subsets
