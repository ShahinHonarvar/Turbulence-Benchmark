
def find_subset_of_length_n(elements):
    subsets = []
    n = 300
    for i in range(1 << len(elements)):
        subset = []
        for j in range(len(elements)):
            if i & (1 << j):
                subset.append(elements[j])
        if len(subset) == n:
            subsets.append(subset)
    return len(subsets)
