
def find_subset_of_length_n(elements, n):
    subsets = []
    for i in range(len(elements)):
        if len(subsets) == n:
            break
        subset = set()
        for j in range(i+1, len(elements)):
            subset.add(elements[j])
            subsets.append(subset)
    return subsets
