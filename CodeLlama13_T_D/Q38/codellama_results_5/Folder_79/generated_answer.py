
def find_subset_of_length_n(elements, n):
    subsets = []
    for i in range(len(elements)):
        subset = elements[:i+1]
        if len(subset) == n:
            subsets.append(subset)
    return subsets
