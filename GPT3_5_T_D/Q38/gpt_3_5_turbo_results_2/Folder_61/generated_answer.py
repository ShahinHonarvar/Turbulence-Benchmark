
def find_subset_of_length_n(elements):
    if len(elements) < 8:
        return 0
    else:
        return math.comb(len(elements), 8)
