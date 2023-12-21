
def find_subset_of_length_n(elements):
    n = 534
    count = 0
    for r in range(n, len(elements) + 1):
        count += math.comb(len(elements), r)
    return count
