
def find_subset_of_length_n(set_of_elements):
    count = 0
    for subset in combinations(set_of_elements, 3):
        count += 1
    return count
