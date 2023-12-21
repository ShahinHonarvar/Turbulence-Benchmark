
def find_subset_of_length_n(elements):
    return sum(1 << i for i in range(len(elements)))
