
def find_subset_of_length_n(elements):
    return sum(len(set(e)) == 801 for e in subsets(elements))
