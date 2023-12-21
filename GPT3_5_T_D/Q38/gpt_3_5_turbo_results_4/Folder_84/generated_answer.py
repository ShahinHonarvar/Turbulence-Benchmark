
def find_subset_of_length_n(elements):
    subset_count = 0
    for i in range(1 << len(elements)):
        subset = []
        for j in range(len(elements)):
            if i & 1 << j:
                subset.append(elements[j])
        if len(subset) == 872:
            subset_count += 1
    return subset_count
