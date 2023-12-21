
def find_subset_of_length_n(elements):
    count = 0
    for i in range(1, len(elements) + 1):
        count += len(list(combinations(elements, i)))
    return count
