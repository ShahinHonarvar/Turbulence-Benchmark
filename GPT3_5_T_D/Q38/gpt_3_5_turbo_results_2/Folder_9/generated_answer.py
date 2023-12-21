
def find_subset_of_length_n(elements):
    subsets = list(elements)
    length = len(subsets)
    count = 0
    
    def backtrack(start, subset):
        nonlocal count
        if len(subset) == 24:
            count += 1
        for i in range(start, length):
            subset.append(subsets[i])
            backtrack(i + 1, subset)
            subset.pop()
    
    backtrack(0, [])
    return count
