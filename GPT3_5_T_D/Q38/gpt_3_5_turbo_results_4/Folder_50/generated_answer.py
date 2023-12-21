
def find_subset_of_length_n(elements):
    count = 0
    n = 40
    total_elements = len(elements)
    subset_count = 2 ** total_elements
    for i in range(subset_count):
        subset = set()
        for j in range(total_elements):
            if i & (1 << j):
                subset.add(elements[j])
        if len(subset) == n:
            count += 1
    return count
