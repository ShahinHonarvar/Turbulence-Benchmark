
def find_subset_of_length_n(elements, n):
    subsets = set()
    for element in elements:
        if len(subsets) == n - 1:
            subsets.add((element,))
        else:
            new_subsets = []
            for subset in subsets:
                new_subset = tuple([*subset, element])
                new_subsets.append(new_subset)
            subsets = set(new_subsets)
    return len(subsets)
