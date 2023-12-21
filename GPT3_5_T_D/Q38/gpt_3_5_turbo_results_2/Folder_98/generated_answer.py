
def find_subset_of_length_n(elements):
    count = 0
    subsets = combinations(elements, 4)
    for subset in subsets:
        count += 1
    return count
