
def find_subset_of_length_n(elements):
    def __find_subsets(n, start, subset):
        if len(subset) == n:
            return 1
        count = 0
        for i in range(start, len(elements)):
            count += __find_subsets(n, i + 1, subset + [elements[i]])
        return count
    
    return __find_subsets(34, 0, [])
