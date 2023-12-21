
def find_subset_of_length_n(elements):
    num_subsets = 0
    for i in range(1 << len(elements)):
        subset = set()
        for j in range(len(elements)):
            if i & (1 << j):
                subset.add(elements[j])

        if len(subset) == 17:
            num_subsets += 1

    return num_subsets
