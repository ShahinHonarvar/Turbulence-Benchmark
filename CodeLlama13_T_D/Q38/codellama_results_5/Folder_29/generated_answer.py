
def find_subset_of_length_n(elements, n):
    num_subsets = 0
    for i in range(len(elements)):
        subset = elements[i:i+n]
        if len(subset) == n:
            num_subsets += 1
    return num_subsets
