
def find_subset_of_length_n(elements, n):
    # base case: if there are no elements left or the current subset size is equal to n, return 1
    if not elements or len(current) == n:
        return 1
    
    # recursive case: try all possible subsets of size n-1 and count the ones that have the same elements as the current subset
    count = 0
    for element in elements:
        count += find_subset_of_length_n(elements - {element}, n-1)
    
    return count
