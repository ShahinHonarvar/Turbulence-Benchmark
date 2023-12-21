
def find_subset_of_length_n(set_of_elements, n):
    subsets = []
    for i in range(len(set_of_elements)):
        subset = set()
        for j in range(i+1):
            subset.add(set_of_elements[j])
        if len(subset) == n:
            subsets.append(subset)
    return subsets
