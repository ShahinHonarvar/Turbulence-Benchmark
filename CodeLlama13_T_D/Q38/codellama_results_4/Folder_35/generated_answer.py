
def find_subset_of_length_n(set_of_elements, n):
    subsets = []
    for i in range(len(set_of_elements)):
        subset = set_of_elements[i:i+n]
        if len(subset) == n:
            subsets.append(subset)
    return len(subsets)
