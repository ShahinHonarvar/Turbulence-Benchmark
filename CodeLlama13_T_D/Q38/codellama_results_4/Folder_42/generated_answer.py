
def find_subset_of_length_n(set_):
    return len([i for i in range(len(set_) + 1) if sum(1 << j - 1 for j in i) == n])
