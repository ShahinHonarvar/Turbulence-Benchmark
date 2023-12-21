
def find_subset_of_length_n(elements):
    subsets = set()
    for i in range(1 << len(elements)):
        subset = []
        for j in range(len(elements)):
            if i & (1 << j):
                subset.append(elements[j])
        if len(subset) == 78:
            subsets.add(tuple(subset))
    return len(subsets)
