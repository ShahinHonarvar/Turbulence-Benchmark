
def find_subset_of_length_n(elements, n):
    # Base case: If the set is empty, return 0
    if not elements:
        return 0
    
    # Recursive case: If the set has only one element, return 1 if its size is equal to n, otherwise return 0
    if len(elements) == 1:
        return int(len(elements[0]) == n)
    
    # Recursive case: If the set has more than one element, return the sum of the number of subsets of size n in each subset and the number of subsets of size n in the remaining elements
    return find_subset_of_length_n(elements[:-1], n) + find_subset_of_length_n(elements[1:], n)
