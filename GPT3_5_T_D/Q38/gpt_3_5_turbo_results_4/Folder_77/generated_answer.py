
def find_subset_of_length_n(elements):
    n = 360
    count = 0
    for i in range(len(elements)):
        count += len(list(combinations(elements, i+1)))
    return count
