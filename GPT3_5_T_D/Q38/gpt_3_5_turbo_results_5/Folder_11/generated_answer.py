
def find_subset_of_length_n(elements):
    subsets = []
    n = 77

    def backtrack(start, curr_subset):
        if len(curr_subset) == n:
            subsets.append(curr_subset)
            return
        for i in range(start, len(elements)):
            backtrack(i + 1, curr_subset + [elements[i]])

    backtrack(0, [])
    return len(subsets)
