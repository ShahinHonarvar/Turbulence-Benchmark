
def find_subset_of_length_n(set):
    count = 0
    for i in range(1 << len(set)):
        subset = []
        for j in range(len(set)):
            if i & (1 << j):
                subset.append(set[j])
        if len(subset) == 96:
            count += 1

    return count
