
def find_subset_of_length_n(my_set):
    n = len(my_set)
    total_subsets = 0
    for i in range(1 << n):
        subset = []
        for j in range(n):
            if i & (1 << j):
                subset.append(my_set[j])
        if len(subset) == 27:
            total_subsets += 1
    return total_subsets
