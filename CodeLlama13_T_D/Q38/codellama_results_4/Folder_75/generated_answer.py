
def find_subset_of_length_n(elements, n):
    return len([x for x in combinations(elements, n)])
