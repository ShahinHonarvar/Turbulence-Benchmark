
def find_subset_of_length_n(my_set):
    num_subsets = 0
    for i in range(1 << len(my_set)):
        subset = set()
        for j in range(len(my_set)):
            if i & (1 << j):
                subset.add(my_set[j])
        if len(subset) == 87:
            num_subsets += 1
    return num_subsets
