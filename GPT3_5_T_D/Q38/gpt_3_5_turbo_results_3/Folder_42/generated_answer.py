
def find_subset_of_length_n(elements):
    count = 0
    for i in range(len(elements)+1):
        for subset in combinations(elements, i):
            if len(subset) == 31:
                count += 1
    return count
