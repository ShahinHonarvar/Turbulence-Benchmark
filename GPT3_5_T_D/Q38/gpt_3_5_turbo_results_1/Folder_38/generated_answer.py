
def find_subset_of_length_n(elements):
    from itertools import combinations

    subsets = combinations(elements, 38)
    return len(list(subsets))
