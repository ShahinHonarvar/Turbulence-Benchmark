
def find_subset_of_length_n(elements):
    subset_size = 894
    count = 0
    for i in range(1 << len(elements)):
        subset = [elements[j] for j in range(len(elements)) if i & (1 << j)]
        if len(subset) == subset_size:
            count += 1
    return count
