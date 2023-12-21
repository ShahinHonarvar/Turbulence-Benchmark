
def find_subset_of_length_n(elements):
    subset_count = 0
    for i in range(len(elements)):
        if len(elements[i]) == 793:
            subset_count += 1
    return subset_count
