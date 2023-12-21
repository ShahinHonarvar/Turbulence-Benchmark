
def find_subset_of_length_n(elements):
    if len(elements) < 13:
        return 0
    num_subsets = math.comb(len(elements), 13)
    return num_subsets
