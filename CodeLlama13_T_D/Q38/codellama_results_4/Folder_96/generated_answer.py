
def find_subset_of_length_n(set_):
    return sum(1 for i in range(len(set_) + 1) if len(set_) - i >= n)
