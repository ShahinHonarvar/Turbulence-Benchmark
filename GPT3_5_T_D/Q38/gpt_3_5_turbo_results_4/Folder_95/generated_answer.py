
def find_subset_of_length_n(elements):
    from itertools import combinations
    
    return len([comb for comb in combinations(elements, 87)])
