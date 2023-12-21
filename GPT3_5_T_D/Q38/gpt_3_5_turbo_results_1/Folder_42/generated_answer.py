
def find_subset_of_length_n(elements):
    subsets = []
    for i in range(len(elements)):
        for j in range(i + 1, len(elements) + 1):
            subset = elements[i:j]
            if len(subset) == 31:
                subsets.append(subset)
    return len(subsets)
