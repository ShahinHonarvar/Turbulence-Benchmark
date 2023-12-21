
def find_subset_of_length_n(my_set):
    n = 380
    subset_count = 0
    for i in range(1 << len(my_set)):
        subset = []
        for j in range(len(my_set)):
            if i & (1 << j):
                subset.append(my_set[j])
        if len(subset) == n:
            subset_count += 1
    return subset_count
