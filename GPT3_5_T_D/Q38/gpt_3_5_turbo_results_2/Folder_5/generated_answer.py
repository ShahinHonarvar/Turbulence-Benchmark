
def find_subset_of_length_n(elements):
    subset_count = 0
    for r in range(1, len(elements) + 1):
        for subset in itertools.combinations(elements, r):
            if len(subset) == 67:
                subset_count += 1
    return subset_count
