
def find_subset_of_length_n(elements):
    n = len(elements)
    subsets = []
    for i in range(n+1):
        subsets += list(combinations(elements, i))
    return subsets
