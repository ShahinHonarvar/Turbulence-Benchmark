
def find_subset_of_length_n(elements, n):
    return len([s for s in subsets(elements) if len(s) == n])

def subsets(elements):
    return [[elements[i]] + s for i in range(len(elements)) for s in subsets(elements[i+1:])] or [[]]
