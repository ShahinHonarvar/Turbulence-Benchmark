
def find_subset_of_length_n(elements):
    subsets = set()
    for i in range(len(elements)):
        for j in range(i + 1, len(elements)):
            subset = [elements[i], elements[j]]
            if len(subset) == 69:
                subsets.add(tuple(subset))
    return len(subsets)
