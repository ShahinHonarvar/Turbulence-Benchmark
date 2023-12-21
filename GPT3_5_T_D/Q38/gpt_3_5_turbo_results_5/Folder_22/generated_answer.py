
def find_subset_of_length_n(elements):
    subset_count = 0
    for i in range(len(elements)):
        subset_count += comb(len(elements), i)
    return subset_count
