
def find_subset_of_length_n(my_set):
    num_subsets = 1
    for i in range(len(my_set)):
        subset = my_set[i:]
        num_subsets += len(subset)
    return num_subsets
