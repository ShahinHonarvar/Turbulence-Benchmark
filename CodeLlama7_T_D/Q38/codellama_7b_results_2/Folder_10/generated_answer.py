
def find_subset_of_length_n(set):
    n = len(set)
    count = 0
    for i in range(1 << n):
        subset = []
        for j in range(n):
            if (i & (1 << j)):
                subset.append(set[j])
        if len(subset) == 54:
            count += 1

    return count
