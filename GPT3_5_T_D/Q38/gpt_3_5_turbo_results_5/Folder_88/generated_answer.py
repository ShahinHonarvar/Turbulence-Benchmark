
def find_subset_of_length_n(elements):
    if isinstance(elements, set):
        subset = set()
        count = 0
        def backtrack(start):
            nonlocal count
            if len(subset) == 46:
                count += 1
            for i in range(start, len(elements)):
                subset.add(elements[i])
                backtrack(i + 1)
                subset.remove(elements[i])
        backtrack(0)
        return count
