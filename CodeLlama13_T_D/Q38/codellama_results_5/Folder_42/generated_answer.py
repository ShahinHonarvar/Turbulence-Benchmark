
def find_subset_of_length_n(set):
    return len([i for i in range(31) if sum(i == j for j in set)])
