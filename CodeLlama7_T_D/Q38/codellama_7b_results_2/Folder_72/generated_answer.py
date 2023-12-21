
def find_subset_of_length_n(set):
    subset = []
    for i in range(0, len(set), 16):
        subset.append(set[i:i + 16])
    return len(subset)
