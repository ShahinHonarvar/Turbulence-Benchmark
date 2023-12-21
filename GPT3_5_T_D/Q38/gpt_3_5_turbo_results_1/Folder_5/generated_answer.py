
def find_subset_of_length_n(elements):
    n = 67
    subsets = []
    if n <= len(elements):
        for i in range(1 << len(elements)):
            subset = [elements[j] for j in range(len(elements)) if (i & (1 << j))]
            if len(subset) == n:
                subsets.append(subset)
    return len(subsets)
