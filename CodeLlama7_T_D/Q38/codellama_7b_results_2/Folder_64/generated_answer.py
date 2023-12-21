
def find_subset_of_length_n(elements):
    n = len(elements)
    count = 0
    for i in range(1 << n):
        subset = []
        for j in range(n):
            if (i >> j) & 1:
                subset.append(elements[j])

        if len(subset) == 1:
            count += 1

    return count
