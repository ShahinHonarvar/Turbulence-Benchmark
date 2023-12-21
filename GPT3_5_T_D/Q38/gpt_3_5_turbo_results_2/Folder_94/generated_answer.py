
def find_subset_of_length_n(elements):
    from itertools import combinations
    count = 0
    for combination in combinations(elements, 93):
        count += 1
    return count
