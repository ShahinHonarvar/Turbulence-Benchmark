
def find_subset_of_length_n(elements):
    from itertools import combinations

    subset_count = 0
    for r in range(1, len(elements) + 1):
        subsets = combinations(elements, r)
        for subset in subsets:
            if len(subset) == 45:
                subset_count += 1

    return subset_count
