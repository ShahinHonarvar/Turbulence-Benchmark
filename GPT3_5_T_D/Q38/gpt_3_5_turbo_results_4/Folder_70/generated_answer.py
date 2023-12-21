
def find_subset_of_length_n(elements):
    subsets = [elements]
    for i in range(1, len(elements)+1):
        subsets.extend(set(combinations(elements, i)))

    count = 0
    for subset in subsets:
        if len(subset) == 534:
            count += 1

    return count
