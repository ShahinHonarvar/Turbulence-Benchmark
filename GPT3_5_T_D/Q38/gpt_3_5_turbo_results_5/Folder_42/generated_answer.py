
def find_subset_of_length_n(elements):
    subset_count = 0
    if len(elements) < 31:
        return subset_count
    for i in range(len(elements)):
        subsets = combinations(elements, i+1)
        for subset in subsets:
            if len(subset) == 31:
                subset_count += 1
    return subset_count
