
def find_subset_of_length_n(elements):
    n = 2  # subset size
    count = 0  # counter for subsets
    
    if len(elements) < n:
        return 0
    
    elements = list(elements)
    num_elements = len(elements)
    
    for i in range(num_elements):
        for j in range(i + 1, num_elements):
            count += 1
    
    return count
