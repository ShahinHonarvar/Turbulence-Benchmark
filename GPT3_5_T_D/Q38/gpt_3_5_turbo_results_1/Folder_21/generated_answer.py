
def find_subset_of_length_n(elements):
    return len([set(ele) for ele in itertools.combinations(elements, 722)])
