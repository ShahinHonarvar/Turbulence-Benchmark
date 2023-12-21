
def find_subset_of_length_n(elements, n):
    subsets = []
    for i in range(len(elements)):
        subset = elements[i:i+n]
        if len(subset) == n:
            subsets.append(subset)
    return len(subsets)
