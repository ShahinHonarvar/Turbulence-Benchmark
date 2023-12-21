
def find_subset_of_length_n(elements):
    from itertools import combinations
    subsets = list(combinations(elements, 56))
    return len(subsets)
