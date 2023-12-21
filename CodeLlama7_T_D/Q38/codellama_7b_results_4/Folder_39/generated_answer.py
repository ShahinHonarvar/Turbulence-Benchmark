
def find_subset_of_length_n(set):
    subset_count = 0
    for i in range(len(set)):
        subset = set[i:]
        if len(subset) == n:
            subset_count += 1

    return subset_count
