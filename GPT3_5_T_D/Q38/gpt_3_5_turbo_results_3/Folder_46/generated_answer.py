
def find_subset_of_length_n(elements):
    subsets = [[]]
    for num in elements:
        new_subsets = []
        for subset in subsets:
            new_subsets.append(subset + [num])
        subsets.extend(new_subsets)
    count = 0
    for subset in subsets:
        if len(subset) == 14:
            count += 1
    return count
