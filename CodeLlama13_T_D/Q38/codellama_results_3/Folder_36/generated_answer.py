
def find_subset_of_length_n(elements, n):
    # Base case: If the set is empty, return 0
    if not elements:
        return 0

    # Recursive case: Add the current element to all subsets of size n-1 and return the count
    return len(elements) * find_subset_of_length_n(elements - {elements[0]}, n-1) + find_subset_of_length_n(elements, n-1)
