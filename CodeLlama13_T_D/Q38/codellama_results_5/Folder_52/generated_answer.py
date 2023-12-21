
def find_subset_of_length_n(elements, n):
    subsets = []
    for i in range(len(elements)):
        if len(subsets) == n:
            break
        subsets.append([elements[i]])
    return len(subsets)
