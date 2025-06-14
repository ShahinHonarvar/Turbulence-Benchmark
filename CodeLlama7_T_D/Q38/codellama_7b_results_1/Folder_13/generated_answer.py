
def find_subset_of_length_n(elements):
    count = 0
    for i in range(1 << len(elements)):
        subset = []
        for j in range(len(elements)):
            if (i >> j) & 1:
                subset.append(elements[j])
        if len(subset) == 801:
            count += 1
    return count
