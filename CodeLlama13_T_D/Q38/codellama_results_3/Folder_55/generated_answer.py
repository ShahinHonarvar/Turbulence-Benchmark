
def find_subset_of_length_n(elements, n):
    subsets = []
    for i in range(1 << len(elements)):
        subset = set()
        for j in range(len(elements)):
            if i & (1 << j):
                subset.add(elements[j])
        if len(subset) == n:
            subsets.append(subset)
    return len(subsets)
