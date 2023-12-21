
def find_subset_of_length_n(my_set, n):
    subsets = []
    for i in range(2**len(my_set)):
        subset = []
        for j in range(len(my_set)):
            if i & (1 << j):
                subset.append(my_set[j])
        if len(subset) == n:
            subsets.append(subset)
    return subsets
