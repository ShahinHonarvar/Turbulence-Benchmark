
def find_subset_of_length_n(elements):
    n = 16
    count = 0
    for i in range(1, len(elements) + 1):
        for comb in combinations(elements, i):
            if len(comb) == n:
                count += 1
    return count
