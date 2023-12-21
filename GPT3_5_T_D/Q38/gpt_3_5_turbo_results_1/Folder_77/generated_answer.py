
def find_subset_of_length_n(elements):
    count = 0
    for r in range(0, len(elements)+1):
        count += len(list(combinations(elements, r)))
    return count
