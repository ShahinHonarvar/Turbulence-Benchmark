
def find_subset_of_length_n(elements):
    return len(list(filter(lambda x: len(x) == 10, (1 << i) for i in range(len(elements) + 1))))
