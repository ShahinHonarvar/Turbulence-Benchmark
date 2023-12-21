
def find_subset_of_length_n(elements):
    subsets = [set()]
    for e in elements:
        new_subsets = []
        for subset in subsets:
            new_subset = subset | {e}
            new_subsets.append(new_subset)
        subsets.extend(new_subsets)
    count = 0
    for subset in subsets:
        if len(subset) == 18:
            count += 1
    return count
