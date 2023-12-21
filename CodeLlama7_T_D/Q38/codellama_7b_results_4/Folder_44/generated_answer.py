
def find_subset_of_length_n(my_set):
    # Initialize a list to store all subsets of size 30
    all_subsets = []
    # Loop through each element in the set
    for element in my_set:
        # Find all subsets of size 30 that include the current element
        subsets = find_subsets_of_length_n(my_set - {element}, 30)
        # Add the current element to each subset
        all_subsets += [[element] + subset for subset in subsets]
    return all_subsets

def find_subsets_of_length_n(my_set, n):
    # Base case: if the set is empty, return an empty list
    if not my_set:
        return []

    # Find all subsets of size n-1 that include the first element of the set
    subsets = find_subsets_of_length_n(my_set - {my_set.pop()}, n-1)
    # Add the first element to each subset
    return [[my_set.pop()] + subset for subset in subsets]
