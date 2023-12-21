
def find_subset_of_length_n(my_set):
    num_subsets = 0
    for i in range(1 << len(my_set)): # bitmask approach
        subset = []
        for j in range(len(my_set)):
            if (i & (1 << j)) > 0: # check if jth bit is set
                subset.append(my_set[j])
        if len(subset) == 97: # only consider subsets of size 97
            num_subsets += 1
    return num_subsets
