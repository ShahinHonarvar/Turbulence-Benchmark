
def find_subset_of_length_n(elements):
    n = 69
    subsets = []
    for i in range(2**len(elements)):
        subset = []
        for j in range(len(elements)):
            if i & (1 << j):
                subset.append(elements[j])
        if len(subset) == n:
            subsets.append(subset)
    return len(subsets)
