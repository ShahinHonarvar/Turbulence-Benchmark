
def find_subset_of_length_n(elements, n):
    subsets = set()
    for element in elements:
        if len(element) == n:
            subsets.add(element)
    return len(subsets)
