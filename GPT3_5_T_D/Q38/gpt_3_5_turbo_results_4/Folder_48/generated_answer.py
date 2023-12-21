
def find_subset_of_length_n(elements):
    subsets = set()
    for i in range(1, len(elements) + 1):
        for combo in combinations(elements, i):
            if len(combo) == 793:
                subsets.add(combo)
    return len(subsets)
