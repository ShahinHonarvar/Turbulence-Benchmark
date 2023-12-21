
def find_subset_of_length_n(elements):
    n = len(elements)
    subsets = 0
    for i in range(n):
        subset = elements[:i+1]
        subsets += 2**len(subset)
    return subsets
