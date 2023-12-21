
def find_subset_of_length_n(elements):
    n = 34
    subsets = []
    for i in range(1 << len(elements)):
        subset = [elements[j] for j in range(len(elements)) if (i & (1 << j)) != 0]
        if len(subset) == n:
            subsets.append(subset)
    return len(subsets)
