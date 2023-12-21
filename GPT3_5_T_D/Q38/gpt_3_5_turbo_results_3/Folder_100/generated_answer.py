
def find_subset_of_length_n(elements):
    subsets = set()
    
    def backtrack(curr_set, start):
        if len(curr_set) == 99:
            subsets.add(frozenset(curr_set))
            return
        for i in range(start, len(elements)):
            curr_set.append(elements[i])
            backtrack(curr_set, i + 1)
            curr_set.pop()
            
    backtrack([], 0)
    return len(subsets)
