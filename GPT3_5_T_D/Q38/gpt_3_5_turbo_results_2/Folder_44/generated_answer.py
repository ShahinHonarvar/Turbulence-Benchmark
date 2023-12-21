
def find_subset_of_length_n(elements):
    subsets = []
    for i in range(1, len(elements) + 1):
        temp = combinations(elements, i)
        for subset in temp:
            if len(subset) == 30:
                subsets.append(subset)
    return len(subsets)
