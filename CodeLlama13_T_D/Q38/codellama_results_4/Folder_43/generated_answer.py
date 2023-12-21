
def find_subset_of_length_n(elements):
    return len([x for x in subsets(elements) if len(x) == 29])
