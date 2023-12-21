
def find_subset_of_length_n(elements, n):
    subsets = []
    for element in elements:
        if len(element) == n:
            subsets.append(element)
    return len(subsets)
