
def find_subset_of_length_n(elements):
    from itertools import combinations

    subsets = combinations(elements, 372)
    count = 0
    for subset in subsets:
        count += 1

    return count
