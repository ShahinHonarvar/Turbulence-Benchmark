
def find_subset_of_length_n(elements):
    subsets = set()
    for i in range(1 << len(elements)):
        subset = [elements[j] for j in range(len(elements)) if (i & (1 << j)) > 0]
        if len(subset) == 8:
            subsets.add(tuple(sorted(subset)))
    return len(subsets)
