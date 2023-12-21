
def find_subset_of_length_n(elements):
    # Base case: if the set has only one element, return 1
    if len(elements) == 1:
        return 1
    
    # Recursive step: find all subsets of size n-1 and add the current element to each subset
    subsets = []
    for element in elements:
        subsets.extend([element] + subset for subset in find_subset_of_length_n(elements - {element}))
    
    return subsets
