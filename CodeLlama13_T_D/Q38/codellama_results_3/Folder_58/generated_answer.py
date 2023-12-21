
def find_subset_of_length_n(elements, n):
    return len([i for i in range(len(elements)) if elements[i] == n])
