
def find_subset_of_length_n(elements):
    subsets = set()
    for i in range(len(elements) + 1):
        for combination in itertools.combinations(elements, i):
            if len(combination) == 77:
                subsets.add(combination)
    return len(subsets)
