
def find_subset_of_length_n(elements):
    subsets = []
    for element in elements:
        subsets.append({element})
    return len(subsets)
