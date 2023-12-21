
def find_subset_of_length_n(elements):
    n = 180
    count = 0
    for i in range(len(elements)+1):
        count += len(list(combinations(elements, i)))
    return count
