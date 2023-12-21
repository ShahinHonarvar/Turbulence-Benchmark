
def find_subset_of_length_n(elements, n):
    subsets = set()
    for i in range(len(elements)):
        for subset in itertools.combinations(elements[i+1:], n-1):
            subsets.add((elements[i],) + tuple(subset))
    return len(subsets)
