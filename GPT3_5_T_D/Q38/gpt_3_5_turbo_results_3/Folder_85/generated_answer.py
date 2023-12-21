
def find_subset_of_length_n(elements):
    count = 0
    for i in range(len(elements)):
        for subset in combinations(elements, 23):
            count += 1
    return count
