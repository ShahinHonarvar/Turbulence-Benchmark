
def find_subset_of_length_n(my_set, n):
    # Initialize a list to store all subsets of size n
    subsets = []

    # Iterate over all elements in the set
    for element in my_set:

        # If the current element is not already in the subset
        if element not in subsets:

            # Add the element to the subset
            subsets.append(element)

    # Initialize a counter variable to keep track of the number of subsets of size n
    count = 0

    # Iterate over all subsets in the list
    for subset in subsets:

        # If the current subset has length n, increment the counter
        if len(subset) == n:

            count += 1

    # Return the number of subsets of size n
    return count
