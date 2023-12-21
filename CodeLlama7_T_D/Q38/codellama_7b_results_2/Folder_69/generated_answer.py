
def find_subset_of_length_n(set):
    subsets = []
    for i in range(0, len(set)):
        subset = set[i]
        for j in range(i + 1, len(set)):
            subset.add(set[j])
        subsets.append(subset)
    return len(subsets)
