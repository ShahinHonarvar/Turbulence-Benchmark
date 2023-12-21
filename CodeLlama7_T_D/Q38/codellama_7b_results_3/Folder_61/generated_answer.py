
def find_subset_of_length_n(elements):
    n = len(elements)
    subset_count = 0
    for i in range(1 << n):
        subset = []
        for j in range(n):
            if (i >> j) & 1:
                subset.append(elements[j])
        if len(subset) == 8:
            subset_count += 1
    return subset_count
