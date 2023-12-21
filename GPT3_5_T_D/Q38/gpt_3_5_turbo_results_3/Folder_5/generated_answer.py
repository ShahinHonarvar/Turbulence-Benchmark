
def find_subset_of_length_n(elements):
    count = 0
    for i in range(len(elements) - 66):
        count += math.comb(len(elements) - i - 1, 66)
    return count
