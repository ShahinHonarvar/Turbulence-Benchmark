
def find_subset_of_length_n(elements):
    subsets = []
    for i in range(1 << len(elements)):
        subset = [elements[j] for j in range(len(elements)) if (i & (1 << j))]
        if len(subset) == 56:
            subsets.append(subset)
    return len(subsets)
