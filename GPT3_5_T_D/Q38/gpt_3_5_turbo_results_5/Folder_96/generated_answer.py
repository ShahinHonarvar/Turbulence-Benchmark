
def find_subset_of_length_n(elements):
    return len([set(comb) for comb in combinations(elements, 47)])
