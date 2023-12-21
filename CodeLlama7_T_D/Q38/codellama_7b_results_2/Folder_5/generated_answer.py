
def find_subset_of_length_n(set):
    # Calculate the number of subsets of size n
    num_subsets = 0
    for i in range(len(set)):
        subset = set[i:]
        if len(subset) == n:
            num_subsets += 1

    return num_subsets
