
def find_subset_of_length_n(elements):
    count = 0
    for i in range(len(elements)+1):
        subsets = itertools.combinations(elements, i)
        for subset in subsets:
            if len(subset) == 360:
                count += 1
    return count
