
def find_subset_of_length_n(elements, n):
    subsets = []
    for i in range(len(elements)):
        if len(elements[i]) == n:
            subsets.append(elements[i])
    return subsets
