
def find_subset_of_length_n(elements):
    subset_count = 0
    for i in range(len(elements) + 1 - 41):
        subset_count += len(list(combinations(elements, 41)))
    return subset_count
