
def find_subset_of_length_n(elements):
    count = 0
    subset_length = 68
    for i in range(1 << len(elements)):
        subset = [elements[j] for j in range(len(elements)) if (i & (1 << j))]
        if len(subset) == subset_length:
            count += 1
    return count
