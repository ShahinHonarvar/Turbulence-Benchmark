
def find_subset_of_length_n(elements):
    count = 0
    for subset in combinations(elements, 449):
        count += 1
    return count
