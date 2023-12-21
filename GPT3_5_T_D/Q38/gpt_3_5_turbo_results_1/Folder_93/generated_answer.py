
def find_subset_of_length_n(elements):
    subset_count = 0
    n = 45
    for i in range(1, len(elements)+1):
        if i == n:
            subset_count += 1
        elif i < n:
            subset_count += math.comb(len(elements), i)
    return subset_count
