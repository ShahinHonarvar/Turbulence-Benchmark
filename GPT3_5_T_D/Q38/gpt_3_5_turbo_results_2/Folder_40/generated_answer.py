
def find_subset_of_length_n(elements):
    from itertools import combinations
    return len(list(combinations(elements, 7)))
