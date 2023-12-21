
def find_subset_of_length_n(elements):
    from itertools import combinations
    count = 0
    for subset in combinations(elements, 300):
        count += 1
    return count
