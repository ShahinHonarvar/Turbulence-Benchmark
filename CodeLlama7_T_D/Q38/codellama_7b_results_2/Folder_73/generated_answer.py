
def find_subset_of_length_n(set):
    n = len(set)
    total = 0
    for i in range(1 << n):
        subset = []
        for j in range(n):
            if (i & (1 << j)):
                subset.append(set[j])
        if len(subset) == 41:
            total += 1

    return total
