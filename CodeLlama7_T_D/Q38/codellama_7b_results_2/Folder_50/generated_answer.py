
def find_subset_of_length_n(my_set, n):
    # Initialize a list to store all subsets of size n
    subsets = []

    # Loop through each element in the set
    for element in my_set:

        # If the current element is not already in the subset, add it
        if element not in subsets:
            subsets.append(element)

        # If the current element is already in the subset, remove it
        else:
            subsets.remove(element)

    # Return the number of all subsets of size n
    return len(subsets)
