
def find_subset_of_length_n(my_set):
    n = len(my_set)
    count = 0
    for i in range(1 << n):
        subset = []
        for j in range(n):
            if i & (1 << j):
                subset.append(my_set[j])
        if len(subset) == n:
            count += 1

    return count
