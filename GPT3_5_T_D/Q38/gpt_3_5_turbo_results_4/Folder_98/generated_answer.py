
def find_subset_of_length_n(elements):
    count = 0
    for subset in combinations(elements, 4):
        count += 1
    return count
