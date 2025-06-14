
def find_subset_of_length_n(elements):
    subset_count = 0
    for i in range(1 << len(elements)):
        subset = set()
        for j in range(len(elements)):
            if (i >> j) & 1:
                subset.add(elements[j])
        if len(subset) == 6:
            subset_count += 1
    return subset_count
